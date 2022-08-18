num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10 #é feita a divisão inteira do algarismo da unidade por 1 e então é tirado o módulo de 10
#(o resto da divisão por 10)
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
