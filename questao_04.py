# Questão 04:

pilha = []
erro = False

exp = input("Digite a expressão a ser verificada: ")

for item in exp:
    if item == '(':
        pilha.append(item)
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            erro = True

if len(pilha) == 0 and not erro:
    print('A expressão está correta')
else:
    print("Erro, a expressão contém caracteres incorretos")