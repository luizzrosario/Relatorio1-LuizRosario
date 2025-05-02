# Importa a classe math para operações mais complexas
import math

# Importa classe para usar o metodo de sair do programa caso exista alguma divisão por zero
import sys

# Função para calcular uma raiz aproximada de uma função pelo metodo da Secante
def secant(a, b, epsilon, fx):
    # Faz a eescrita no arquivo txt do cabeçalho dos dados
    with open("secante-res.txt", "w") as file:
        file.write("xn\t\t\t\t\t\tf(xn)\n")
        file.write(f"{a:6f}\t\t\t\t")
        x = a
        file.write(f"{eval(fx):6f}\n")

    # Loop para aproximar a raiz
    while(True):
        # Valor de xk-1
        x = a
        f1 = eval(fx)

        # Valor de xk
        x = b
        f2 = eval(fx)

        # Escreve no arquivo os dados que estão sendo gerados a cada iteração
        with open("secante-res.txt", "a") as file:
            file.write(f"{b:6f}\t\t\t\t")
            file.write(f"{f2:6f}\n")

        # Se o valor da função no xk seja menor ou igual a tolerancia o algoritmo retorna o xk
        if module(f2) <= epsilon:
             return b

        # Guardao anterior do xk para que na proxima iteração ele seja o xk-1
        b_temp = b

        # Retorna um erro e sai do programa caso tenha uma divisão por zero
        if a == b:
             print("Can't devide by zero!\n")
             sys.exit()

        # Calcula o xk+1
        b = (f2 * a - f1 * b) / (f2 - f1)

        # xk agora se torna xk-1
        a = b_temp


# Retorna o modulo de um número
def module(x):
    if x < 0:
        return (-1 * x)

    return x

# Faz a leitura do arquivo onde estão os dados
with open("secante-fun.txt", "r") as file:
    lines = file.readlines()

# Pega a função na primeira linha do arquivo
func = lines[0].rstrip()

# Pega o valor de a e b na segunda linha
a_str, b_str = lines[1].split()

a = float(a_str)
b = float(b_str)

# Pega o valor do epsilon na ultima linha
epsilon = float(lines[2])

# Pega o retorno da função com o valor da raiz aproximada
answer = secant(a, b, epsilon, func)

# Escreve o valor da raiz aproximada no arquivo
with open("secante-res.txt", "a") as file:
            file.write(f"Raiz aproximada = {answer:6f}")