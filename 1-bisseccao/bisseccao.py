import math  # Importa a biblioteca para operações matemáticas


# Função que calcula uma raiz aproximada usando o método da bisseção
def bisseccao(inicio, fim, tolerancia, expressao):
    # Avalia os extremos do intervalo
    x = inicio
    f_inicio = eval(expressao)
    x = fim
    f_fim = eval(expressao)

    if f_inicio * f_fim > 0:
        raise ValueError(
            "O intervalo não contém mudança de sinal. Escolha outro intervalo."
        )

    # Cria o arquivo de saída com o cabeçalho
    with open("bisseccao-res.txt", "w") as arquivo:
        arquivo.write("a\t\t\tb\t\t\tf(a)\t\tf(b)\t\t(b-a)\t\t(b-a)/a\t\tx\t\t\tf(x)\n")

    while True:
        x = (inicio + fim) / 2
        x_temp = x  # Backup de x

        x = inicio
        f_inicio = eval(expressao)

        x = fim
        f_fim = eval(expressao)

        x = x_temp
        f_meio = eval(expressao)

        # Protege contra divisão por zero se inicio == 0
        taxa_relativa = (fim - inicio) / inicio if inicio != 0 else 0

        with open("bisseccao-res.txt", "a") as arquivo:
            arquivo.write(f"{inicio:6f}\t")
            arquivo.write(f"{fim:6f}\t")
            arquivo.write(f"{f_inicio:6f}\t")
            arquivo.write(f"{f_fim:6f}\t")
            arquivo.write(f"{(fim - inicio):6f}\t")
            arquivo.write(f"{taxa_relativa:6f}\t")
            arquivo.write(f"{x:6f}\t")
            arquivo.write(f"{f_meio:6f}\n")

        # Condição de parada (f(x) pequena ou intervalo pequeno)
        if modulo(f_meio) <= tolerancia or (fim - inicio) / 2 < tolerancia:
            return x

        if f_inicio * f_meio < 0:
            fim = x
        else:
            inicio = x


# Valor absoluto
def modulo(valor):
    return abs(valor)


# Lê a função e os dados de entrada
with open("bisseccao-fun.txt", "r") as arquivo:
    linhas = arquivo.readlines()

expressao = linhas[0].strip()
inicio_str, fim_str = linhas[1].split()
inicio = float(inicio_str)
fim = float(fim_str)
tolerancia = float(linhas[2])

try:
    # Executa o método e salva o resultado
    raiz_aproximada = bisseccao(inicio, fim, tolerancia, expressao)

    with open("bisseccao-res.txt", "a") as arquivo:
        arquivo.write(f"\nRaiz aproximada = {raiz_aproximada:6f}")
except Exception as erro:
    print(f"Erro: {erro}")
