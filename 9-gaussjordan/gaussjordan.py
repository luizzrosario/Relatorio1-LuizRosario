import numpy as np

# Lê a matriz do arquivo "gaussjordan-mat.txt"
with open("gaussjordan-mat.txt", "r") as arquivo:
    tamanho = int(arquivo.readline().strip())  # Lê o tamanho da matriz (n x n)
    matriz_original = []
    for _ in range(tamanho):
        linha = list(map(float, arquivo.readline().strip().split()))
        matriz_original.append(linha)

# Cria a matriz aumentada [A | I], onde I é a identidade
A = np.array(matriz_original)
identidade = np.identity(tamanho)
aumentada = np.hstack((A, identidade))

# Aplica o método de Gauss-Jordan para obter a inversa de A
for i in range(tamanho):
    pivo = aumentada[i, i]

    if pivo == 0:
        raise ValueError("A matriz não é inversível (pivô zero).")

    # Normaliza a linha do pivô
    aumentada[i, :] /= pivo

    # Zera os elementos acima e abaixo do pivô
    for j in range(tamanho):
        if i != j:
            multiplicador = aumentada[j, i]
            aumentada[j, :] -= multiplicador * aumentada[i, :]

# A parte direita da matriz aumentada agora é a inversa de A
matriz_inversa = aumentada[:, tamanho:]

# Salva a matriz inversa no arquivo "gaussjordan-res.txt"
with open("gaussjordan-res.txt", "w") as arquivo:
    for linha in matriz_inversa:
        linha_formatada = " ".join(f"{valor:.3f}" for valor in linha)
        arquivo.write(linha_formatada + "\n")
