# Troca duas linhas da matriz se o pivô de uma delas for zero
def trocar_linhas(matriz, linha1, linha2):
    matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]
    return matriz


# Resolve o sistema linear a partir da matriz já escalonada (triangular superior)
def resolver_substituicao_inversa(matriz):
    n = len(matriz)
    resultado = [0] * n

    # Calcula os valores de xn até x0
    for i in range(n - 1, -1, -1):
        resultado[i] = matriz[i][n] / matriz[i][i]
        for j in range(i - 1, -1, -1):
            matriz[j][n] -= matriz[j][i] * resultado[i]

    return resultado


# Aplica o método da eliminação de Gauss para escalonar a matriz
def eliminacao_gauss(matriz):
    tamanho = len(matriz)
    linha = 0

    while linha < tamanho - 1:
        pivo = matriz[linha][linha]

        # Se o pivô for zero, procura outra linha com pivô válido para trocar
        if pivo == 0:
            nova_linha = linha
            while nova_linha < tamanho:
                if matriz[nova_linha][linha] != 0:
                    break
                nova_linha += 1
            matriz = trocar_linhas(matriz, linha, nova_linha)

        # Zera os elementos abaixo do pivô
        for k in range(linha + 1, tamanho):
            multiplicador = matriz[k][linha] / matriz[linha][linha]
            linha_temp = [val * multiplicador for val in matriz[linha]]
            matriz[k] = [a - b for a, b in zip(matriz[k], linha_temp)]

        linha += 1

    return matriz


# Lê a matriz aumentada do arquivo
matriz = []
with open("eliminacaogauss-mat.txt", "r") as arquivo:
    for linha in arquivo:
        valores = list(map(float, linha.split()))
        matriz.append(valores)

# Escalona a matriz e resolve o sistema
matriz_escalonada = eliminacao_gauss(matriz)
solucao = resolver_substituicao_inversa(matriz_escalonada)

# Salva a matriz escalonada e a solução no arquivo
with open("eliminacaogauss-res.txt", "w") as arquivo:
    for linha in matriz_escalonada:
        arquivo.write(" ".join(map(str, linha)) + "\n")
    for i, valor in enumerate(solucao):
        arquivo.write(f"x{i} = {valor}\n")
