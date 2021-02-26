# Questão 10:

estoq = {'tomate': [1000, 2.30],
            'alface': [500, 0.45],
            'batata': [2001, 1.20],
            'feijão': [100, 1.50]
            }


total = 0

while True:
    prod = input('Digite o nome do produto ou fim para sair: ')
    if prod == 'fim':
        break
    if prod in estoq:
        quant = int(input('Quantidade:'))    
        if quant <= estoq[prod][0]:
            preco = estoq[prod][1]
            custo = preco * quant
            print(f'{prod:12s}:{quant:3d} x {preco:6.2f} = {custo:6.2f}')
            estoq[prod][0] -= quant
            total += custo
        else:
            print('Quantidade solicitada não disponivel')
    else:
        print('O produto não consta no estoque')

print(f'Custo total das compras ficou em:{total:21.2f} <--\n')
print('Estoque restante:\n')
for chave, dados in estoq.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço:{dados[1]:6.2f}\n')