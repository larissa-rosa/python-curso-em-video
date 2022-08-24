n = c = soma = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'A soma dos {c} valores digitados é {soma}')
