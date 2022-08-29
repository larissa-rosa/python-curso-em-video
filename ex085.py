lista = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}° número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Lista completa: {lista}')
lista[0].sort()
print(f'Lista dos números pares: {lista[0]}')
lista[1].sort()
print(f'Lista dos número ímpares: {lista[1]}')