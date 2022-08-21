menor = 0
maior = 0

for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if c == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {}'.format(menor))
print('O maior peso é {}'.format(maior))

