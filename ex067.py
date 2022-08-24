n = 0
while n >= 0:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    c = 0
    while c <= 10:
        print(f'{c:2} x {n} = {n * c:2}')
        c += 1
print('Programa encerrado')
