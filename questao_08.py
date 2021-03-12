# Questão 08:

t = [-10, -8, 0, 1, 2, 5, -2, -4]

mini = t[0]
max = t[0]
soma = 0

for e in t:
    if mini > e:
        mini = e

    if max < e:
        max = e

    soma += e

media = soma / len(t)

print("{} é a menor temperatura. {} é a maior temperatura. {} é a temperatura média.".format(mini, max, media))