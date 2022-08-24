total = mil = menor = c = 0
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    c += 1
    if c == 1 or valor < menor:
        menor = valor
        barato = produto
    if valor > 1000:
        mil += 1
    total += valor

    continuar = str(input('Deseja continuar? [S/N]')).strip()[0]
    while not continuar in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]')).strip()[0]
    if continuar in 'Nn':
        break

print(f'O valor total da compra é R${total}')
print(f'{mil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato custa R${menor:.2f} e é {barato}.')
