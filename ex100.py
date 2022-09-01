from random import randint

def sorteia(lista):
    print(f'Números sorteados: ', end='')
    for c in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
        print(f'{n}', end=' ')
    print()

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares de {lista} é {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)


