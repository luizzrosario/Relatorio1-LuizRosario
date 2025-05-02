import math  # Biblioteca para funções matemáticas


# Função que calcula uma raiz aproximada usando o método da posição falsa
def posicao_falsa(inicio, fim, tolerancia, expressao):
    # Cria o arquivo de saída com cabeçalho das colunas
    with open("posicaofalsa-res.txt", "w") as arquivo:
        arquivo.write(
            "a\t\t\t\tb\t\t\t\tf(a)\t\t\tf(b)\t\t\t(b-a)\t\t\tc\t\t\t\tf(c)\n"
        )

    while True:
        # Calcula f(a)
        x = inicio
        f_inicio = eval(expressao)

        # Calcula f(b)
        x = fim
        f_fim = eval(expressao)

        # Estima a raiz com a fórmula da posição falsa
        c = (inicio * f_fim - fim * f_inicio) / (f_fim - f_inicio)

        # Calcula f(c)
        x = c
        f_c = eval(expressao)

        # Registra os dados da iteração
        with open("posicaofalsa-res.txt", "a") as arquivo:
            arquivo.write(f"{inicio:6f}\t\t")
            arquivo.write(f"{fim:6f}\t\t")
            arquivo.write(f"{f_inicio:6f}\t\t")
            arquivo.write(f"{f_fim:6f}\t\t")
            arquivo.write(f"{(fim - inicio):6f}\t\t")
            arquivo.write(f"{c:6f}\t\t")
            arquivo.write(f"{f_c:6f}\n")

        # Verifica se a tolerância foi atingida
        if modulo(f_c) <= tolerancia:
            return c

        # Atualiza os limites do intervalo com base no sinal de f(c)
        if f_c < 0:
            inicio = c
        else:
            fim = c


# Retorna o valor absoluto de um número
def modulo(valor):
    return -valor if valor < 0 else valor


# Lê a função e os parâmetros do arquivo
with open("posicaofalsa-fun.txt", "r") as arquivo:
    linhas = arquivo.readlines()

expressao = linhas[0].strip()
inicio_str, fim_str = linhas[1].split()
inicio = float(inicio_str)
fim = float(fim_str)
tolerancia = float(linhas[2])

# Executa o método da posição falsa
raiz_aproximada = posicao_falsa(inicio, fim, tolerancia, expressao)

# Escreve o resultado final no arquivo
with open("posicaofalsa-res.txt", "a") as arquivo:
    arquivo.write(f"Raiz aproximada = {raiz_aproximada:6f}")
