print('### Progressão aritmética ###')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
print('10 primeiros termos da PA: ')
c = 0
while c < 10:
    print('{} '.format(termo), end='')
    termo += razao
    c += 1