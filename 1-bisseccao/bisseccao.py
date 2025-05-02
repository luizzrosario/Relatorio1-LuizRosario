# Importa a classe math para calculos matematicos mais complexos como seno, cosseno e tangente ou outras operações
import math

# Função para calcular uma raiz aproximada de de uma função pelo metodo da bissecção
def bissection(a, b, epsilon, fx):
    # Escreve o cabeçalho do arquivo de resposta
    with open("bisseccao-res.txt", "w") as file:
        file.write("a				b				f(a)			f(b)			(bk-ak)			(bk-ak)/ak		x				f(x)\n")

    # Laço de repertição para calcular a raiz aproximada
    while(True):
        x = (a + b) / 2 # Valor da possivel raiz
        fx = eval(func) # Valor da função na possivel raiz

        x_temp = x # Variavel temporaria para a possivel raiz

        # Valor de na função
        x = a
        fa = eval(func)

        # Valor de b na função
        x = b
        fb = eval(func)

        # Devolve o valor anterior para x
        x = x_temp

        # Escreve os resultados de iteração no arquivo como 6 digitos de precisão
        with open("bisseccao-res.txt", "a") as file:
            file.write(f"{a:6f}\t\t")
            file.write(f"{b:6f}\t\t")
            file.write(f"{fa:6f}\t\t")
            file.write(f"{fb:6f}\t\t")
            file.write(f"{(b - a):6f}\t\t")
            file.write(f"{((b - a) / a):6f}\t\t")
            file.write(f"{x:6f}\t\t")
            file.write(f"{fx:6f}\n")

        # Se o modulo do resultado da função na possivel raiz for menor ou igual a tolerancia o algoritmo vai retornar esse x como raiz aproximada
        if module(fx) <= epsilon:
            return x

        # Caso o valor da função na possivel raiz seja negativo o valor de "a" será substituido por x
        # Caso não seja negativo o valor de a continua o mesmo e o valor de "b" será trocado por x
        if fx < 0:
            a = x
            b = b
        else:
            a = a
            b = x

# Retorna o modulo de um número
def module(x):
    if x < 0:
        return (-1 * x)

    return x

# Faz a leitura da função no arquivo
with open("bisseccao-fun.txt", "r") as file:
    lines = file.readlines()

# Pega a função do arquivo
func = lines[0].rstrip()

# a e b são os intervalos da raiz
a_str, b_str = lines[1].split()

a = float(a_str)
b = float(b_str)

# Condição de parada
epsilon = float(lines[2])

# Raiz aproximada
answer = bissection(a, b, epsilon, func)

# Escreve o resultado no arquivo de resposta com 6 digitos de precisão
with open("bisseccao-res.txt", "a") as file:
            file.write(f"Raiz aproximadda = {answer:6f}")