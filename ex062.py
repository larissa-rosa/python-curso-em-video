print('### Progressão aritmética ###')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
print('10 primeiros termos da PA: ')
c = 0
total = 0
maistermos = 10
while maistermos != 0:
    total += maistermos
    while c < total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    maistermos = int(input('Quantos outros termos você gostaria de ver? '))
print('Progressão finalizada com {} termos.'.format(c))


