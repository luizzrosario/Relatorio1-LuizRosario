import numpy as np

# Carrega os dados do arquivo em uma matriz
with open("jacobi-mat.txt") as file:
    lines = file.readlines()

# Lê a tolerância de erro da primeira linha do arquivo
tolerancia = float(lines[0])

# Resto do arquivo contém os coeficientes da matriz e os valores do lado direito
matriz = []
for line in lines[1:]:
    matriz.append(list(map(float, line.split())))

# Converte a matriz em um array numpy
matriz = np.array(matriz)
n = len(matriz)

# Monta a estrutura da matriz para o método de Jacobi
jacobi = np.zeros((n, n + 1))
for i in range(n):
    jacobi[i, :] = matriz[i, :] / matriz[i, i]
    jacobi[i, n] = matriz[i, n] / matriz[i, i]
    jacobi[i, i] = 0

jacobi = -jacobi
jacobi[:, n] = -jacobi[:, n]
resultados = np.copy(jacobi[:, n])
jacobi = jacobi[:, :-1]

# Verifica se a matriz é diagonalmente dominante
diagonalmente_dominante = all(
    abs(matriz[i, i]) >= np.sum(np.abs(matriz[i, :-1])) - abs(matriz[i, i])
    for i in range(n)
)

# Se não for dominante, salva aviso no arquivo e encerra
if not diagonalmente_dominante:
    with open("jacobi-res.txt", "w") as file:
        file.write(
            "A matriz não é diagonalmente dominante. O método pode não convergir.\n"
        )
    exit()

# Inicializa o vetor solução
x = np.zeros(n)
iteracoes = 0

# Iterações do método de Jacobi
while True:
    x_anterior = x.copy()
    x = np.dot(jacobi, x) + resultados
    iteracoes += 1
    erro = np.linalg.norm(x - x_anterior)
    if erro < tolerancia:
        break

# Salva as soluções no arquivo
with open("jacobi-res.txt", "w") as file:
    for i in range(n):
        file.write(f"x{i + 1} = {x[i]}\n")
    file.write(f"iteracoes necessarias: {iteracoes}\n")
