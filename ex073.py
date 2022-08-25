times = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Atlético Mineiro',
             'Corinthians', 'Flamengo', 'Botafogo', 'Atlético Paranaense',
             'Internacional', 'São Paulo', 'Fluminense', 'Vasco da Gama',
             'Chapecoense', 'Sport', 'Ponte Preta', 'Coritiba', 'Vitória',
             'Figueirense', 'Atlético Goianense')
print(f'Os 5 primeiros colocados no Campeonato Brasileiro de Futebol de 2018 foram {times[0:5]}')
print(f'Os últimos 4 colocados foram {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense estava em {times.index("Chapecoense")+1}° lugar.')
