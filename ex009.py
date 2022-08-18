numero = int(input('Digite um número: '))

print('A tabuada de {} é:\n'.format(numero))
print('-'*15)
print(' 1x{} = {:2}\n'
      ' 2x{} = {:2}\n'
      ' 3x{} = {:2}\n'
      ' 4x{} = {:2}\n'
      ' 5x{} = {:2}\n'
      ' 6x{} = {:2}\n'
      ' 7x{} = {:2}\n'
      ' 8x{} = {:2}\n'
      ' 9x{} = {:2}\n'
      '10x{} = {:2}'
      .format(numero, numero*1, numero, numero*2, numero, numero*3, numero, numero*4, numero, numero*5,
              numero, numero*6, numero, numero*7, numero, numero*8, numero, numero*9, numero, numero*10))
print('-'*15)
