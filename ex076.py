listagem = ('Pão', 5.65,
            'Bolo', 15,
            'Sonho', 4,
            'Croissant', 9.75,
            'Chocolate', 6.95,
            'Torta de limão', 45)
print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<33}', end='')
    else:
        print(f'R${listagem[c]:5.2f}')
print('-'*40)
