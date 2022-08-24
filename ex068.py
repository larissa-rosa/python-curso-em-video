from random import randint
jogador = 0
escolha = 'par'
venceu = 0
jogo = True

while jogo == True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip()
    computador = randint(0, 100)
    total = jogador + computador

    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'O total deu {total}.')


    if computador % 2 == 0 and jogador % 2 == 0 or computador % 2 != 0 and jogador % 2 != 0:
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
        jogo = False
        print(f'Game over! Você venceu {venceu} vezes!')