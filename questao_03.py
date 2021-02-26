# Questão 03:

listaA = [1, 2, 3, 4,  5]
listaB = [2, 4, 6, 8, 10]
listaC = []

for i in listaA:
    if i not in listaC:
        listaC.append(i)
        for x in listaB:
            if x not in listaC:
                listaC.append(x)


print('A lista resultante é: ', listaC)