import math  # Biblioteca para operações matemáticas
import sys  # Usada para encerrar o programa em caso de erro crítico


# Função que aplica o método da Secante para encontrar uma raiz aproximada
def metodo_secante(x_antigo, x_atual, tolerancia, expressao):
    # Cria o arquivo e escreve o cabeçalho
    with open("secante-res.txt", "w") as arquivo:
        arquivo.write("x_n\t\t\t\tf(x_n)\n")
        x = x_antigo
        arquivo.write(f"{x_antigo:6f}\t\t{eval(expressao):6f}\n")

    while True:
        x = x_antigo
        f_antigo = eval(expressao)

        x = x_atual
        f_atual = eval(expressao)

        # Salva os valores da iteração
        with open("secante-res.txt", "a") as arquivo:
            arquivo.write(f"{x_atual:6f}\t\t{f_atual:6f}\n")

        # Verifica critério de parada
        if modulo(f_atual) <= tolerancia:
            return x_atual

        # Evita divisão por zero
        if f_atual == f_antigo:
            print("Erro: divisão por zero detectada!")
            sys.exit()

        # Atualiza o próximo valor de x usando a fórmula da secante
        proximo_x = (f_atual * x_antigo - f_antigo * x_atual) / (f_atual - f_antigo)

        # Atualiza os valores para a próxima iteração
        x_antigo = x_atual
        x_atual = proximo_x


# Retorna o valor absoluto de um número
def modulo(valor):
    return -valor if valor < 0 else valor


# Lê os dados do arquivo de entrada
with open("secante-fun.txt", "r") as arquivo:
    linhas = arquivo.readlines()

expressao = linhas[0].strip()
x1_str, x2_str = linhas[1].split()
x_inicial = float(x1_str)
x_segundo = float(x2_str)
tolerancia = float(linhas[2])

# Executa o método e obtém a raiz aproximada
raiz_aproximada = metodo_secante(x_inicial, x_segundo, tolerancia, expressao)

# Registra o valor final da raiz no arquivo
with open("secante-res.txt", "a") as arquivo:
    arquivo.write(f"Raiz aproximada = {raiz_aproximada:6f}")
