import math
import numpy as np


# Verifica se os vetores são suficientemente próximos (critério de parada)
def convergiu(x_antigo, x_novo, epsilon):
    erro = sum(abs(a - b) for a, b in zip(x_antigo, x_novo))
    return erro < epsilon


# Método de Gauss-Jacobi para resolver sistemas lineares
def gauss_jacobi(A, b, max_iteracoes, epsilon):
    n = len(b)
    x = b.copy()

    # Verifica se os pivôs não são nulos para evitar divisão por zero
    for i in range(n):
        if abs(A[i][i]) == 0:
            return None  # Não dá pra continuar com pivô nulo
        x[i] = b[i] / A[i][i]  # Chute inicial

    for _ in range(max_iteracoes):
        x_novo = x.copy()

        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - soma) / A[i][i]

        if convergiu(x, x_novo, epsilon):
            x = x_novo
            break

        x = x_novo

    return x


# Lê a matriz A e o vetor B do arquivo
with open("gaussseidel-mat.txt", "r") as arquivo:
    linhas = [linha.strip() for linha in arquivo if linha.strip()]
    A = np.array([list(map(float, linha.split())) for linha in linhas[:-1]])
    B = np.array(list(map(float, linhas[-1].split())))

# Aplica o método de Gauss-Jacobi
solucao = gauss_jacobi(A, B, max_iteracoes=10, epsilon=0.01)

# Escreve os resultados em um arquivo
with open("gaussseidel-res.txt", "w") as arquivo:
    for i, valor in enumerate(solucao):
        arquivo.write(f"x{i} = {valor}\n")
