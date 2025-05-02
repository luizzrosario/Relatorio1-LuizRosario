import numpy as np

# Leitura dos dados de entrada
with open('gaussjordan-mat.txt', 'r') as arquivo:
    n = int(arquivo.readline().strip())
    A = []
    for i in range(n):
        linha = list(map(float, arquivo.readline().strip().split()))
        A.append(linha)


# Cálculo da matriz inversa
n = len(np.array(A))
matriz = np.hstack((np.array(A), np.identity(n)))

for i in range(n):
    pivo = matriz[i, i]
        
    if pivo == 0:
        raise ValueError("A matriz não é inversível.")
        
    matriz[i, :] /= pivo

    for j in range(n):
        if i != j:
            fator = matriz[j, i]
            matriz[j, :] -= fator * matriz[i, :]

resultado = matriz[:, n:]

# Salvar o resultado no arquivo "gaussjordan-res.txt"
with open('gaussjordan-res.txt', 'w') as arquivo:
    for linha in resultado:
        linha_formatada = ' '.join([f'{valor:.3f}' for valor in linha])
        arquivo.write(linha_formatada + '\n')