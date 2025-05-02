# Metodo para trocar uma linha por outra caso o pivor de uma das linhas da array seja zero
def replaceline(array, line1, line2):
    array[line1], array[line2] = array[line2], array[line1]

    # Retorna o array
    return array

# Metodo Fatoração LU
def lufactorization(array):
    size = len(array) # Tamanho do array(número de linhas)
    # Contadores para linhas e colunas
    i = 0
    j = 0
    mtpl = []

    # Loop para alterar as linhas da matriz
    while(j < size):
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
            mtpl.append(multiplicator)

            arraytemp = [element * multiplicator for element in array[i]]
            array[k] = [a - b for a, b in zip(array[k], arraytemp)]
            k = k + 1

        i = i + 1
        
    return array, mtpl # Retorna o array escalonado e um vetor com os multiplicadores

array = [] # Array onde vai ser guardada a matriz
multiplicator = [] # Vetor onde os multiplicadores serão guardados
b = [] # Vetor onde os termos independentes das equações serão guardados

# Abre o aquivo em que está a matriz e guarda na variavel array
with open("fatoracaoLU-mat.txt", 'r') as file:
    linhas = file.readlines()

    # Encontrar a quebra de linha
    idx_quebra = linhas.index('\n')

    # Ler a matriz
    for linha in linhas[:idx_quebra]:
        elementos = linha.strip().split(' ')
        array.append([float(elemento) for elemento in elementos if elemento])

    # Ler os valores de b
    for linha in linhas[idx_quebra+1:]:
        b.extend([float(elemento) for elemento in linha.strip().split(' ') if elemento])

array, multiplicator = lufactorization(array) # Array atualizado com a matriz escalonada e os multiplicadores

# Este pedaço de codigo organiza a matriz onde os multiplicadores vão ficar
size = len(array)
l = [[None] * size for _ in range(size)]
i = 0
k = 0
while(i < size):
    j = 0

    # Monta a matriz com os multiplicdores na diagonal inferior, 1 na diagonal principal e zeros na diagonal superior
    while(j < size):
        if i == j:
            l[i][j] = 1
        elif i > j:
            l[i][j] = multiplicator[k]
            k = k + 1
        else:
            l[i][j] = 0
        j = j + 1
    i = i + 1

# Cria um arquivo com a matriz escalonada, a matriz com os multiplicadores e com o valor dos termos independentes
with open("fatoracaoLU-res.txt", 'w') as file:
    # Escreve a matriz escalonada no arquivo
    for line in array:
        line_format = ' '.join(map(str, line))
        file.write(line_format + '\n')
    
    # Pula uma linha
    file.write('\n')
    
    # Escreve a matriz com os multiplicadores no arquivo
    for line in l:
        line_format = ' '.join(map(str, line))
        file.write(line_format + '\n')
    
    # Pula uma linha
    file.write('\n')
    
    # Escreve os coeficientes independentes
    file.write(f'B = {b}')