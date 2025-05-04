import numpy as np

# Lê os dados da matriz aumentada do sistema
matriz = np.loadtxt('fatoracaoLU-mat.txt')
n = len(matriz)
num_colunas = matriz.shape[1]

b = matriz[:, -1]             # Termos independentes
U = matriz[:, :-1].copy()     # Coeficientes da matriz

valores_L = []

# Transformação de Gauss para tornar U triangular superior
for i in range(n):
    linha_pivo = max(range(i, n), key=lambda j: abs(U[j][i]))
    U[[i, linha_pivo]] = U[[linha_pivo, i]]

    for j in range(i + 1, n):
        m = U[j][i] / U[i][i]
        valores_L.append(m)
        U[j] -= m * U[i]

# Constrói a matriz L com os multiplicadores calculados
L = np.identity(n)
k = 0
for i in range(1, n):
    for j in range(i):
        L[i][j] = valores_L[k]
        k += 1

# Resolve L * y = b
y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

# Resolve U * x = y
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i][i]

# Salva as soluções no arquivo de saída
with open("fatoracaoLU-res.txt", "w") as file:
    for i in range(n):
        file.write(f'x{i + 1} = {x[i]}\n')
