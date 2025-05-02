import math  # Importa a biblioteca para operações matemáticas


# Função que calcula uma raiz aproximada usando o método da bisseção
def bisseccao(inicio, fim, tolerancia, expressao):
    # Cria o arquivo de saída com o cabeçalho
    with open("bisseccao-res.txt", "w") as arquivo:
        arquivo.write(
            "a\t\t\t\tb\t\t\t\tf(a)\t\t\tf(b)\t\t\t(b-a)\t\t\t(b-a)/a\t\t\tx\t\t\t\tf(x)\n"
        )

    while True:
        x = (inicio + fim) / 2  # Calcula o ponto médio
        x_temp = x  # Salva temporariamente

        x = inicio
        f_inicio = eval(expressao)

        x = fim
        f_fim = eval(expressao)

        x = x_temp
        f_meio = eval(expressao)

        # Registra os dados da iteração no arquivo
        with open("bisseccao-res.txt", "a") as arquivo:
            arquivo.write(f"{inicio:6f}\t\t")
            arquivo.write(f"{fim:6f}\t\t")
            arquivo.write(f"{f_inicio:6f}\t\t")
            arquivo.write(f"{f_fim:6f}\t\t")
            arquivo.write(f"{(fim - inicio):6f}\t\t")
            arquivo.write(f"{((fim - inicio) / inicio):6f}\t\t")
            arquivo.write(f"{x:6f}\t\t")
            arquivo.write(f"{f_meio:6f}\n")

        # Verifica se encontrou a raiz dentro da tolerância
        if modulo(f_meio) <= tolerancia:
            return x

        # Atualiza os limites do intervalo
        if f_meio < 0:
            inicio = x
        else:
            fim = x


# Retorna o valor absoluto
def modulo(valor):
    return -valor if valor < 0 else valor


# Lê os dados do arquivo de entrada
with open("bisseccao-fun.txt", "r") as arquivo:
    linhas = arquivo.readlines()

expressao = linhas[0].strip()
inicio_str, fim_str = linhas[1].split()
inicio = float(inicio_str)
fim = float(fim_str)
tolerancia = float(linhas[2])

# Executa o método e salva o resultado
raiz_aproximada = bisseccao(inicio, fim, tolerancia, expressao)

with open("bisseccao-res.txt", "a") as arquivo:
    arquivo.write(f"Raiz aproximada = {raiz_aproximada:6f}")
