n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

op = 0
while op != 5:
    print('\n[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos Números\n'
          '[5] Sair do Programa\n')
    op = int(input('Qual operação você deseja realizar? '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif op == 2:
        prod = n1 * n2
        print('O produto entre {} e {} é {}.'.format(n1, n2, prod))
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}.'.format(n2, n1))
        else:
            print('{} é igual a {}'.format(n1, n2))
    elif op == 4:
        n1 = float(input('\nDigite o novo primeiro valor: '))
        n2 = float(input('Digite o novo segundo valor: '))
    elif op != 5:
        print('\nValor inválido!')
print('\nFim do programa.')
