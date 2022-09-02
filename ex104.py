def leiaint(msg):
    ok = False
    valor = 0
    while not ok:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mValor inválido\033[m')
    return valor


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
