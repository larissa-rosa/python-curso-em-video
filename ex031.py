#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para
# viagens mais longas.

distancia = float(input('Qual a distância da viagem (km)? '))

passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('O valor de sua passagem será de R${:.2f}'.format(passagem))