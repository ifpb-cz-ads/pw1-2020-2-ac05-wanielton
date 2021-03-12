# Questão 09:

text = input("Digite a frase a ser analisada: ").replace(" ", "")
dicio = {}

for i in text:
    if i in dicio:
        dicio[i]= dicio[i]+1
    else:
        dicio[i] = 1
print(dicio)