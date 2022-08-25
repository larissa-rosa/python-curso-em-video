from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100),
               randint(1, 100), randint(1, 100))
print(f'Os números sorteados foram ', end='')
for c in numeros:
    print(f'{c}', end=' ')
print(f'\nO menor número gerado foi o {min(numeros)}, e o maior foi o {max(numeros)}.')