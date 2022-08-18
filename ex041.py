from datetime import date

nascimento = int(input('Qual o ano de nascimento do atleta? '))

idade = date.today().year - nascimento

print('Idade:', idade)
if idade <= 9:
    print('Categoria: mirim')
elif idade <= 14:
    print('Categoria: infantil')
elif idade <= 19:
    print('Categoria: junior')
elif idade <= 25:
    print('Categoria: sênior')
else:
    print('Categoria: master')