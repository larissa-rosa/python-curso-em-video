from random import randint
venceu = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    while not escolha in 'PpIi':
        print('Valor inválido.')
        escolha = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    computador = randint(0, 100)
    total = jogador + computador

    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'O total deu {total}.')

    if total % 2 == 0:
        resultado = 'par'
        print('Deu par!')
    else:
        resultado = 'impar'
        print('Deu ímpar!')

    if escolha in 'Pp' and resultado == 'par' or escolha in 'Ii' and resultado == 'impar':
        print('Você venceu!')
        venceu += 1
    else:
        print(('Você perdeu!'))
        print(f'Game over! Você venceu {venceu} vezes!')
        break