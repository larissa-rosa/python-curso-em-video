peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em m: '))

imc = peso / (altura ** 2)

print('Seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')