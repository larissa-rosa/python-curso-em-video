lista = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Valor adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Valores digitados em ordem crescente: {lista[0:]}')