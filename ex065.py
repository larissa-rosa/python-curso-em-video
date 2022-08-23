r = True
soma = c = menor = maior = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Você quer digitar mais um valor? [S/N] ')).strip()[0]
    soma += n
    c += 1
    if c == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
print('Você digitou {} números, e a média entre eles foi {}.'.format(c, soma / c))
print('O menor valor lido foi {}, e o maior valor lido foi {}.'.format(menor, maior))
