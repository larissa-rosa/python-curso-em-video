velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade <= 80:
    print('Está dentro do limite de velocidade.')
else:
    print('Está acima do limite de velocidade.')
    multa = (velocidade - 80) * 7
    print('Você vai ter que pagar uma multa de R${:.2f}'.format(multa))