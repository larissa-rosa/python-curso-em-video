from random import randint
from time import sleep
computador = randint(0,5) #número int aleatório entre 0 e 5

print('Vou pensar em um número entre 0 e 5...')

jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('Você adivinhou! Eu pensei no número {}'.format(computador))
else:
    print('Você errou! Eu pensei no número {}'.format(computador))
