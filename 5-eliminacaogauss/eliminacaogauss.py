# Metodo para trocar uma linha por outra caso o pivor de uma das linhas da array seja zero
def replaceline(array, line1, line2):
    array[line1], array[line2] = array[line2], array[line1]

    # Retorna o array
    return array

# Metodo para pegar o array com a matriz escalonada e transforma em um resultado no formato x0, x1, ..., xn
def substituicao_inversa(matriz):
    n = len(matriz)
    solucao = [0] * n

    # Pega o resultado com baase na matriz escalonada
    for i in range(n - 1, -1, -1):
        solucao[i] = matriz[i][n] / matriz[i][i]
        for j in range(i - 1, -1, -1):
            matriz[j][n] -= matriz[j][i] * solucao[i]

    return solucao # Retorna a solução do sistema

# Metodo da eliminação de Gauss
def gausselimination(array):
    size = len(array) # Tamanho do array(número de linhas)
    # Contadores para linhas e colunas
    i = 0
    j = 0

    # Loop para alterar as linhas da matriz
    while(j < size - 1):
        pivot = array[i][i] # Pivor da matriz

        # Caso o pivor seja zero, a linha em que ele está sera trocada
        if(pivot == 0):
            k = i

            # Procura uma linha em que o pivor não seja zero
            while(k < size):
                if array[k][i] != 0.0:
                    break
                k = k + 1

            array = replaceline(array, k, i) # Pega a nova matriz com as linhas trocadas

        j = i + 1

        k = j # Contador para as linhas

        # Loop para zerar a coluna abaixo do pivor
        while(k < size):
            multiplicator = array[k][i] / pivot

            arraytemp = [element * multiplicator for element in array[i]]
            array[k] = [a - b for a, b in zip(array[k], arraytemp)]
            k = k + 1

        i = i + 1
        
    return array # Retorna o array escalonado
        

array = [] # Array onde vai ser guardada a matriz

# Abre o aquivo em que está a matriz e guarda na variavel array
with open("eliminacaogauss-mat.txt", 'r') as file:
    for line in file:
        element = line.split()
        line_convert = [float(elemento) for elemento in element]
        array.append(line_convert)

array = gausselimination(array) # Array atualizado com a matriz escalonada
answer = substituicao_inversa(array) # Vetor com a solução

# Cria um arquivo com a matriz escalonada e com a resposta
with open("eliminacaogauss-res.txt", 'w') as file:
        # Escreve a matriz no arquivo
        for line in array:
            line_format = ' '.join(map(str, line))
            file.write(line_format + '\n')
        
        i = 0 # Contador

        # Escreve os resultados nos sistemas
        for element in answer:
            file.write(f"x{i} = " + str(element) + '\n')
            i = i + 1