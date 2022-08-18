'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor
 do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores
 ou iguais, o aumento é de 15%.'''

salarioAtual = float(input('Salário do funcionário: R$'))

if salarioAtual > 1250:
    aumento = 0.1
else:
    aumento = 0.15

novoSalario = salarioAtual + (aumento * salarioAtual)

print('O novo salário do funcionário é de R${:.2f}'.format(novoSalario))