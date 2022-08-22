from random import randint
from time import sleep
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10...')
sleep(2)
jogador = int(input('Adivinhe o número em que pensei: '))
tentativas = 1
while computador != jogador:
    print('O número em que você pensou foi {}? '.format(jogador))
    tentativas += 1
    if computador != jogador:
        if computador > jogador:
            jogador = int(input('Mais... Tente novamente: '))
        elif computador < jogador:
            jogador = int(input('Menos... Tente novamente: '))
print('O número em que você pensou foi {}? '.format(jogador))
print('Parabéns! Você adivinhou na {}ª tentativa!'.format(tentativas))

