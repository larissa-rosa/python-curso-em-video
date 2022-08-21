somaidades = 0
maisvelho = 0
nomemaisvelho = ''
mulheresmenores = 0

for c in range(0, 4):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c+1))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c+1)))
    sexo = str(input('Digite o sexo (F ou M) da {}ª pessoa: '.format(c+1))).upper()
    somaidades += idade
    if c == 0 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenores += 1

print('A média das idades do grupo é {}.'.format(somaidades/4))
print('O homem mais velho é o {}, com {} anos.'.format(nomemaisvelho, maisvelho))
print('Ao todo, {} mulher(es) têm menos de 20 anos.'.format(mulheresmenores))
