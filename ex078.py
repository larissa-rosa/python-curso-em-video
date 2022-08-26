lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = maior = lista[c]
        menorpos = maiorpos = c
    else:
        if lista[c] < menor:
            menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]
print(f'Valores digitados: {lista}')

print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
