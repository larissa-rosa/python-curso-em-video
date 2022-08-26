lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} valores.')
print(f'Valores digitados em ordem decrescente: {lista}')
if 5 in lista:
        print('O número 5 está na lista.')
else:
        print('O número 5 não está na lista.')
