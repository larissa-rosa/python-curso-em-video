valornormal = float(input('Qual o valor do produto? R$'))
pagamento = int(input('Qual a forma de pagamento?\n'
                      '1 - à vista (dinheiro ou cheque) - 10% de desconto\n'
                      '2 - à vista no cartão - 5% de desconto\n'
                      '3 - em até 2x no cartão\n'
                      '4 - 3x ou mais no cartão - 20% de acréscimo\n'))

if pagamento == 1:
    valorfinal = valornormal - (0.1 * valornormal)
elif pagamento == 2:
    valorfinal = valornormal - (0.05 * valornormal)
elif pagamento == 3:
    valorfinal = valornormal
elif pagamento == 4:
    valorfinal = valornormal + (0.2 * valornormal)
else:
    print('O valor digitado é inválido')

print('O valor a ser pago é de R${:.2f}'.format(valorfinal))


