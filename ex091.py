from random import randint
from operator import itemgetter

jogo = { 'Primeiro jogador': randint(1, 6),
         'Segundo jogador': randint(1, 6),
         'Terceiro jogador': randint(1, 6),
         'Quarto jogador': randint(1, 6)}
ranking = list()

print('='*40)
print(f'{"Valores Tirados no Dado":^40} ')
print('='*40)
for k, v in jogo.items():
    print(f'{k} tirou {v}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('='*40)
print(f'{"Ranking":^40} ')
print('='*40)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')
