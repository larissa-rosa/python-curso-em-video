soma = 0
for c in range(0, 6):
    numero = int(input('Digite o {}º valor: '.format(c+1)))
    if numero % 2 == 0:
        soma += numero
print('\nA soma dos números pares é {}'.format(soma))
