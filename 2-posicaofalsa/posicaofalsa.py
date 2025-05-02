# Importa a classe math para calculos matematicos mais complexos como seno, cosseno e tangente ou outras operações
import math

# Função para calcular uma raiz aproximada de de uma função pelo metodo da posição falça
def falseposition(a, b, epsilon, func):
    # Escreve o cabeçalho do arquivo de resposta
    with open("posicaofalsa-res.txt", "w") as file:
        file.write("a				b				f(a)			f(b)			(bk-ak)         ck			    f(ck)\n")

    # Laço de repertição para calcular a raiz aproximada
    while(True):
        # Valor de na função
        x = a
        fa = eval(func)

        # Valor de b na função
        x = b
        fb = eval(func)

        c = (a * fb - b * fa) / (fb - fa)

        x = c
        fc = eval(func)

        # Escreve os resultados de iteração no arquivo como 6 digitos de precisão
        with open("posicaofalsa-res.txt", "a") as file:
            file.write(f"{a:6f}\t\t")
            file.write(f"{b:6f}\t\t")
            file.write(f"{fa:6f}\t\t")
            file.write(f"{fb:6f}\t\t")
            file.write(f"{(b - a):6f}\t\t")
            file.write(f"{c:6f}\t\t")
            file.write(f"{fc:6f}\n")

        # Se o modulo do resultado da função na possivel raiz for menor ou igual a tolerancia o algoritmo vai retornar esse x como raiz aproximada
        if module(fc) <= epsilon:
            return c

        # Caso o valor da função na possivel raiz seja negativo o valor de "a" será substituido por x
        # Caso não seja negativo o valor de a continua o mesmo e o valor de "b" será trocado por x
        if fc < 0:
            a = c
            b = b
        else:
            a = a
            b = c

# Retorna o modulo de um número
def module(x):
    if x < 0:
        return (-1 * x)

    return x

# Faz a leitura da função no arquivo
with open("posicaofalsa-fun.txt", "r") as file:
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
answer = falseposition(a, b, epsilon, func)

# Escreve o resultado no arquivo de resposta com 6 digitos de precisão
with open("posicaofalsa-res.txt", "a") as file:
            file.write(f"Raiz aproximadda = {answer:6f}")