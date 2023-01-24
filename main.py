a, b = map(
    int,
    input(
        'Digite o comprimento de X e Y das matrizes que deseja realizar a subtração: '
    ).split())

matrizA = []
matrizB = []
matrizC = []
linhaA = []
linhaB = []

for l in range(a):
    linhaA = list(
        map(
            int,
            input(
                'Digite os números existentes nesta linha da primeira matriz: '
            ).split()))[:b]
    matrizA.append(linhaA)
for l in range(a):
    linhaB = list(
        map(
            int,
            input(
                'Digite os números existentes nesta linha da segunda matriz: '
            ).split()))[:b]
    matrizB.append(linhaB)

for i in range(a):
    matrizC.append([])
    for j in range(b):
        linhac = matrizA[i][j] - matrizB[i][j]
        matrizC[i].append(linhac)

for l in matrizC:
    for c in l:
        print(c, end=' ')
    print('\n')

    print('Essa é a matriz resultante da subtração!')
