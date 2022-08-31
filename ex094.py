pessoa = {}
grupo = []
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Valor inválido!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Deseja continuar? ')).strip()[0]
    if continuar not in 'SsNn':
        print('Valor inválido!')
        continuar = str(input('Deseja continuar? ')).strip()[0]
    if continuar in 'Nn':
        break
print(f'{len(grupo)} pessoas foram cadastradas')
media = soma / len(grupo)
print(f'Média de idade: {media:.1f}')
print(f'Mulheres cadastradas: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\nPessoas acima da média de idade: ', end='')
for p in grupo:
    if p['idade'] > media:
        print(p['nome'], end=' ')