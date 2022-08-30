lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break

print('='*40)
print(f'{"Boletim":^40}')
print('='*40)
print(f'{"Índice":<6}{"Nome":^29}{"Média":>5}')
for i, a in enumerate(lista):
    print(f'{i:<6}{a[0]:^29}{a[2]:>5}')

while True:
    indice = int(input('Deseja ver as notas de qual aluno? (Digite o índice ou 999 para parar) '))
    if indice == 999:
        break
    if indice < len(lista):
        print(f'Notas de {lista[indice][0]} foram {lista[indice][1]}')