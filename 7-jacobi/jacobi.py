# Importa pacotes para usar dentro do codigo
import numpy as np
import math

# Metodo para descobrir se a condição de parada da convergência foi atingida 
def comparar(x, xk, eps):
    sum = 0
    zip_object = zip(x, xk)

    for list1_i, list2_i in zip_object:
        sum = sum + math.fabs(list1_i - list2_i)

    if (sum < eps):
        return True
    else:
        return False   

# Metodo para calcular as soluções do sistema
def jacobi(A, b, maxiter, eps):
    n = len(b)
    sol = True
    x = b.copy()

    for i in list(range(1, n + 1, 1)):
        if (math.fabs(A[i - 1][i-1]) > 0.0):
            x[i - 1] = b[i - 1] / A[i - 1][i - 1]
        else:
            sol = False
            break
  
    if(sol):
        xk = x.copy()
        iter = 0
 
        while(iter < maxiter):
            iter = iter + 1

            for i in list(range(1, n + 1, 1)):
                s = 0

                for j in list(range(1, n + 1, 1)):
                    if ((i - 1) != (j - 1)):
                        s = s + A[i - 1][j - 1] * x[j - 1]

                xk[i - 1] = (1 / A[i - 1][i - 1]) * (b[i - 1] - s)
     
            if comparar(x, xk, eps):
                x = xk.copy()
                break    

            x = xk.copy()

    return x

# Faz a leitura do arquivo onde tem a matriz com os coeficientes das equações
with open("jacobi-mat.txt", 'r') as file:
    lines = file.readlines()

# Coloca os valores dentro das variaveis array para a matriz e vector para o vetor onde tem os termos independentes
lines = [line.strip() for line in lines if line.strip()]
array = np.array([list(map(float, line.split())) for line in lines[:-1]])
vector = np.array(list(map(float, lines[-1].split())))

# answer possui os valores de x
answer = jacobi(array, vector, 10, 0.01)

# Abre o arquivo jacobi-res.txt para escrever os resultados
with open("jacobi-res.txt", 'w') as file:
        i = 0 # Contador

        # Escreve os resultados dos sistemas
        for element in answer:
            file.write(f"x{i} = " + str(element) + '\n')
            i = i + 1