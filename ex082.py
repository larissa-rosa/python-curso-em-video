numero = []
par = []
impar = []
while True:
    numero.append(int(input('Digite um número: ')))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print(f'Números digitados: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')

