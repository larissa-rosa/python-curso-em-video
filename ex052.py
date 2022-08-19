numero = int(input('Digite um número para descobrir se é primo: '))

primo = True
for c in range(1, numero+1):
    if numero % c == 0 and c != 1 and c != numero or numero == 1:
        primo = False

if primo:
    print('O número {} é primo.'.format(numero))
else:
    print('O número {} não é primo.'.format(numero))


