numeros = (int(input(f'Digite o primeiro número: ')),
           int(input(f'Digite o segundo número: ')),
           int(input(f'Digite o terceiro número: ')),
           int(input(f'Digite o quarto número: ')))
print(f'Tupla: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3)}.')
else:
    print('O número 3 não apareceu em nenhuma posição.')

print(f'Os números pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
