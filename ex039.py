from datetime import date

nascimento = int(input('Digite o seu ano de nascimento: '))

idade = date.today().year - nascimento

print('Quem nasceu em {} completa {} anos em {}.'.format(nascimento, idade, date.today().year))
if idade == 18:
    print('Está na hora de se alistar no serviço militar.')
elif idade < 18:
    tempo = 18 - idade
    print('Falta(m) {} ano(s) para você se alistar no serviço militar.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você deveria ter se alistado há {} ano(s) no serviço militar.'.format(tempo))