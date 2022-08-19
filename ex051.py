'''print('### Progressão aritmética ###')
inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('10 primeiros termos da PA: ')

for c in range(0, 10):
    termos = inicio + c * razao
    print(termos)'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('Primeiros 10 termos da progressão aritmética:')
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('Fim!')
