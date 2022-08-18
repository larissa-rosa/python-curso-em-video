from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
jogador = int(input('[0] Pedra\n'
                    '[1] Papel\n'
                    '[2] Tesoura\n'
                    'Qual é a sua jogada? \n'))

print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))


if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('O jogador venceu!')
    elif jogador == 2:
        print('O computador venceu!')
elif computador == 1:
    if jogador == 0:
        print('O computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('O jogador venceu!')
elif computador == 2:
    if jogador == 0:
        print('O jogador venceu!')
    elif jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('Empate!')

