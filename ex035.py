print('== Analisador de triângulos ==')
s1 = float(input('Digite o tamanho do primeiro segmento: '))
s2 = float(input('Digite o tamanho do segundo segmento: '))
s3 = float(input('Digite o tamanho do terceiro segmento: '))

if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
    print(('Os segmentos acima NÃO podem formar um triângulo'))
else:
    print('Os segmentos acima podem formar um triângulo')
