#financiamento bancário

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Tempo (em anos) de financiamento: '))

prestação = valor / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de R${:.2f}.'.format(valor, anos, prestação))

if prestação <= (0.3 * salario):
    print('Empréstimo pode ser concedido.')
else:
    print('Empréstimo negado.')

