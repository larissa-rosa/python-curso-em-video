dados = list()
listagem = list()
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))

    if len(listagem) == 0:
        maiorpeso = menorpeso = dados[1] #peso
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
           menorpeso = dados[1]

    listagem.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break

print(f'Ao todo, {len(listagem)} pessoas foram cadastradas.')

print(f'O maior peso foi {maiorpeso} kg, peso de ', end='')
for p in listagem:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]')

print(f'O menor peso foi {menorpeso} kg, peso de ', end='')
for p in listagem:
    if p[1] == menorpeso:
        print(f'[{p[0]}]')
