import numpy as np

# Lê os dados do arquivo
with open('gaussseidel-mat.txt') as file:
    lines = file.readlines()

# Primeira linha: tolerância do erro
tolerancia = float(lines[0])

# Demais linhas: coeficientes da matriz aumentada
matriz = [list(map(float, line.split())) for line in lines[1:]]
matriz = np.array(matriz)
n = len(matriz)

# Prepara a matriz para o método de Gauss-Seidel
gauss_seidel = np.zeros((n, n + 1))
for i in range(n):
    gauss_seidel[i, :] = matriz[i, :] / matriz[i, i]
    gauss_seidel[i, n] = matriz[i, n] / matriz[i, i]
    gauss_seidel[i, i] = 0  # zera o coeficiente da diagonal principal

# Separa os termos independentes e ajusta os sinais
gauss_seidel = -gauss_seidel
gauss_seidel[:, n] = -gauss_seidel[:, n]
resultados = np.copy(gauss_seidel[:, n])
gauss_seidel = gauss_seidel[:, :-1]

# Verifica convergência pelo critério das linhas (diagonal dominante)
dominante = all(abs(matriz[i, i]) >= np.sum(np.abs(matriz[i, :-1])) - abs(matriz[i, i]) for i in range(n))
if not dominante:
    with open("gaussseildel-res.txt", "w") as file:
        file.write("A matriz não é diagonalmente dominante. O método de Gauss-Seidel pode não convergir.\n")
    exit()

# Iterações do método
x = np.zeros(n)
iteracoes = 0
while True:
    anterior = x.copy()
    for i in range(n):
        x[i] = np.dot(gauss_seidel[i, :], x) + resultados[i]
    iteracoes += 1
    erro = np.linalg.norm(x - anterior)
    if erro < tolerancia:
        break

# Gera o texto das soluções
solucoes = [f'x{i + 1} = {x[i]}' for i in range(n)]

# Salva os resultados
with open("gaussseidel-res.txt", "w") as file:
    file.write('\n'.join(solucoes))
    file.write(f'\niteracoes necessarias: {iteracoes}')
