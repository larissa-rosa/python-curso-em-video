n = int(input('Digite um número para visualizar o seu fatorial: '))
res = 1
c = n
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    res *= c
    c -= 1
print(res)
