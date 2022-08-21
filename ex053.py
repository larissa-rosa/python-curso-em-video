frase = str(input('Escreva uma frase: ')).strip().lower()

lista = frase.split()
junto = ''.join(lista)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
   inverso += junto[c]
print(junto, inverso)


if junto == inverso:
    print('A frase "{}" é um palíndromo.'.format(frase))
else:
    print('A frase "{}" não é um palíndromo.'.format(frase))

