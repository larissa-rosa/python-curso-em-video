numero = int(input('Digite um número para visualizar sua tabuada: '))

print('\nA tabuada de {} é:'.format(numero))

for c in range(0, 11):
    print('{:2} x {} = {:2}'.format(c, numero, c * numero))

