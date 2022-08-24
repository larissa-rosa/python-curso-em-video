c = 1
maiores = mulheres = homens = 0
while True:
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [F/M]: '.format(c))).strip()[0]
    while not sexo in 'FfMm':
        print('Sexo inválido.')
        sexo = str(input('Sexo da {}ª pessoa [F/M]: '.format(c))).strip()[0]
    c += 1

    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

    continuar = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip()[0]
    while not continuar in 'SsNn':
        print('Resposta inválida.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break

print(f'{maiores} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres têm menos de 20 anos.')