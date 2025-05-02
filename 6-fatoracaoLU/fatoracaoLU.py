# Troca duas linhas da matriz se o pivô de uma delas for zero
def trocar_linhas(matriz, linha1, linha2):
    matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]
    return matriz


# Aplica o método de Fatoração LU e retorna a matriz U e os multiplicadores
def fatoracao_lu(matriz):
    tamanho = len(matriz)
    multiplicadores = []
    linha = 0

    while linha < tamanho:
        pivo = matriz[linha][linha]

        # Troca de linha se o pivô for zero
        if pivo == 0:
            nova_linha = linha
            while nova_linha < tamanho:
                if matriz[nova_linha][linha] != 0:
                    break
                nova_linha += 1
            matriz = trocar_linhas(matriz, linha, nova_linha)

        for k in range(linha + 1, tamanho):
            fator = matriz[k][linha] / matriz[linha][linha]
            multiplicadores.append(fator)
            linha_temp = [valor * fator for valor in matriz[linha]]
            matriz[k] = [a - b for a, b in zip(matriz[k], linha_temp)]

        linha += 1

    return matriz, multiplicadores


# Lê a matriz A e o vetor B a partir do arquivo
matriz = []
b = []
with open("fatoracaoLU-mat.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    idx_quebra = linhas.index("\n")  # Encontra a linha em branco

    # Lê a matriz A
    for linha in linhas[:idx_quebra]:
        valores = list(map(float, linha.strip().split()))
        matriz.append(valores)

    # Lê o vetor B
    for linha in linhas[idx_quebra + 1 :]:
        b.extend(map(float, linha.strip().split()))

# Aplica a fatoração LU
matriz_u, multiplicadores = fatoracao_lu(matriz)

# Monta a matriz L com os multiplicadores
tamanho = len(matriz_u)
matriz_l = [[0] * tamanho for _ in range(tamanho)]
indice = 0

for i in range(tamanho):
    for j in range(tamanho):
        if i == j:
            matriz_l[i][j] = 1
        elif i > j:
            matriz_l[i][j] = multiplicadores[indice]
            indice += 1
        else:
            matriz_l[i][j] = 0

# Escreve os resultados no arquivo
with open("fatoracaoLU-res.txt", "w") as arquivo:
    # Matriz U (escalonada)
    for linha in matriz_u:
        arquivo.write(" ".join(map(str, linha)) + "\n")
    arquivo.write("\n")

    # Matriz L
    for linha in matriz_l:
        arquivo.write(" ".join(map(str, linha)) + "\n")
    arquivo.write("\n")

    # Vetor B
    arquivo.write(f"B = {b}\n")
