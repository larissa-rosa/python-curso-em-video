frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1)) #posição em Python + 1 = posição real
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1)) #encontra a última ocorrência do termo
