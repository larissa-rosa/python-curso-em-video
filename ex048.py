soma = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
print('Soma de todos os múltiplos de 3 que são ímpares, no intervalo de 1 a 500: {}'.format(soma))
