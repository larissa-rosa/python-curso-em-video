from datetime import date

maiores = 0
menores = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c+1)))
    if (date.today().year - nascimento) >= 18:
        maiores += 1
    else:
        menores += 1
print('O número de pessoas que já atingiram a maioridade é {}'.format(maiores))
print('O número de pessoas que ainda não atingiram a maioridade é {}.'.format(menores))
