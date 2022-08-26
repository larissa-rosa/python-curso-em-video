lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não será adicionado.')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
lista.sort()
print(f'Lista dos valores em ordem crescente: {lista}')

