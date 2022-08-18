from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa é de {}'.format(hypot(co, ca)))