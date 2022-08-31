dados = {}
pontos = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Número de partidas jogadas: '))

for c in range(0, partidas):
    pontos.append(int(input(f'Número de gols na partida {c+1}: ')))

dados['gols'] = pontos[:]
dados['total'] = sum(pontos)

print('='*40)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
print('='*40)
print(dados)

print('='*40)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas')
print('='*40)

for i, v in enumerate(dados['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')
print('='*40)
