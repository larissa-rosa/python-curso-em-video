# um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preço = dias * 60 + 0.15 * km
print('O preço a ser pago é de R${:.2f}'.format(preço))