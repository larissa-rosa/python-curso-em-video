from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo: '))

sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Seno: {}\nCosseno: {}\nTangente: {}'.format(sin, cos, tan))

