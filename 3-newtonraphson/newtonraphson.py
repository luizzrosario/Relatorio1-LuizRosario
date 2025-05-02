import math  # Biblioteca para operações matemáticas


# Função que calcula uma raiz aproximada usando o método de Newton-Raphson
def newton_raphson(inicio, fim, tolerancia, expressao, derivada):
    # Cria o arquivo com o cabeçalho dos resultados
    with open("newtonraphson-res.txt", "w") as arquivo:
        arquivo.write("x_n\t\t\t\tf(x_n)\n")

    # Começa pelo ponto médio entre os extremos
    x = (inicio + fim) / 2

    while True:
        f_x = eval(expressao)

        # Registra os valores a cada iteração
        with open("newtonraphson-res.txt", "a") as arquivo:
            arquivo.write(f"{x:6f}\t\t{f_x:6f}\n")

        # Verifica se já atingiu a precisão desejada
        if modulo(f_x) <= tolerancia:
            return x

        # Atualiza o valor de x usando a fórmula do método
        x = x - (eval(expressao) / eval(derivada))


# Retorna o valor absoluto de um número
def modulo(valor):
    return -valor if valor < 0 else valor


# Lê os dados do arquivo de entrada
with open("newtonraphson-fun.txt", "r") as arquivo:
    linhas = arquivo.readlines()

expressao = linhas[0].strip()  # Função original
derivada_expr = linhas[1].strip()  # Derivada da função
inicio_str, fim_str = linhas[2].split()
inicio = float(inicio_str)
fim = float(fim_str)
tolerancia = float(linhas[3])  # Critério de parada

# Executa o método de Newton-Raphson
raiz_aproximada = newton_raphson(inicio, fim, tolerancia, expressao, derivada_expr)

# Escreve o resultado final no arquivo
with open("newtonraphson-res.txt", "a") as arquivo:
    arquivo.write(f"Raiz aproximada = {raiz_aproximada:6f}")
