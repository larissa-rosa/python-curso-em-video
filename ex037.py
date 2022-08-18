numero = int(input('Escolha um número inteiro: '))
base = int(input('Escolha a base de conversão:\n'
                 '1 - binário\n'
                 '2 - octal\n'
                 '3 - hexadecimal\n'))

if base == 1:
    print('O número decimal {} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O número decimal {} convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O número decimal {} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Valor inválido')
