dados = {}
pontos = []
time = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Número de partidas jogadas: '))
    pontos.clear()
    for c in range(0, partidas):
        pontos.append(int(input(f'Número de gols na partida {c+1}: ')))
    dados['gols'] = pontos[:]
    dados['total'] = sum(pontos)
    time.append(dados.copy())
    while True:
        continuar = str(input('Deseja adicionar mais jogadores? [S/N] ')).strip()[0]
        if continuar in 'SsNn':
            break
        else:
            print('Resposta inválida!')
    if continuar in 'Nn':
        break
print('='*40)
print(f'cód ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Código inválido!')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('='*40)
