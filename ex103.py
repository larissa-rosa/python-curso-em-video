def ficha(nome='null', gols=0):
    return print(f'O jogador {nome} fez {gols} gols no campeonato')


jogador = str(input('Nome do jogador: '))
numero = str(input('Número de gols feitos: '))
if numero.isnumeric():
    numero = int(numero)
else:
    numero = 0
if jogador.strip() == '':
    ficha(gols=numero)
else:
    ficha(jogador, numero)

