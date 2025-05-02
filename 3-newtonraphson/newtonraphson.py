# Importa a classe math para operações mais complexas
import math

# Função para calcular uma raiz aproximada de uma função pelo metodo Newton Raphson
def newtonRaphson(a, b, epsilon, fx, fxl):
    # Faz a eescrita no arquivo txt do cabeçalho dos dados
    with open("newtonraphson-res.txt", "w") as file:
        file.write("xn\t\t\t\tf(xn)\n")

    # Pega a mediana entre os pontos "a" e "b"
    x = (a + b) / 2

    # Loop para aproximar a raiz
    while(True):
        f = eval(fx)

        # Escreve no arquivo os dados que estão sendo gerados nas iterações
        with open("newtonraphson-res.txt", "a") as file:
            file.write(f"{x:6f}\t\t")
            file.write(f"{f:6f}\n")

        # Se o valor da função na possivel raiz for menor ou igual a tolerancia(condição de parada) o algoritmo retorna o valor x
        if module(f) <= epsilon:
            return x

        # Calcula o novo valor de x com base em f(x) e f'(x)
        x = x - (eval(fx) / eval(fxl))

# Retorna o modulo de um número
def module(x):
    if x < 0:
        return (-1 * x)

    return x

# Faz a leitura do arquivo onde estão os dados
with open("newtonraphson-fun.txt", "r") as file:
    lines = file.readlines()

# Pega a função na primeira linha do arquivo
func = lines[0].rstrip()

# Pega a derivada da função na segunda linha do arquivo
df = lines[1].rstrip()

# Pega o valor de "a" e "b" na terceira linha
a_str, b_str = lines[2].split()

a = float(a_str)
b = float(b_str)

# Pega o valor do epsilon na ultima linha
epsilon = float(lines[3])

# Pega o retorno da função com o valor da raiz aproximada
answer = newtonRaphson(a, b, epsilon, func, df)

# Escreve o valor da raiz aproximada no arquivo
with open("newtonraphson-res.txt", "a") as file:
            file.write(f"Raiz aproximada = {answer:6f}")