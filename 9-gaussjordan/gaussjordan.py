import numpy as np

# Lê os dados do arquivo
with open("gaussjordan-mat.txt") as file:
    lines = file.readlines()

# Primeira linha: tolerância do erro
tolerancia = float(lines[0])

# Demais linhas: coeficientes da matriz aumentada
matriz = [list(map(float, line.split())) for line in lines[1:]]
matriz = np.array(matriz)
n = len(matriz)

# Método de Gauss-Jordan
for i in range(n):
    # Faz a diagonal principal igual a 1
    matriz[i, :] /= matriz[i, i]
    # Elimina os coeficientes abaixo e acima da diagonal
    for j in range(n):
        if i != j:
            matriz[j, :] -= matriz[j, i] * matriz[i, :]

# Extraímos as soluções da última coluna
solucoes = [f"x{i + 1} = {matriz[i, n]}" for i in range(n)]

# Salva as soluções em um arquivo "output.txt"
with open("gaussjordan-res.txt", "w") as file:
    file.write("\n".join(solucoes))
