n = int(input('Quantos elementos da sequência de Fibonacci você deseja visualizar? '))
f1 = 0
f2 = 1
print('{} {} '.format(f1, f2), end='')
c = 3
while c <= n:
    f3 = f1 + f2
    print('{} '.format(f3), end='')
    f1 = f2
    f2 = f3
    c += 1

