matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna = maiorvalor = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um elemento para a posição [{i}, {j}] da matriz: '))
        if matriz[i][j] % 2 == 0:
            somapares += matriz[i][j]
        if j == 2:
            somacoluna += matriz[i][j]
        if matriz[1][j] > maiorvalor:
            maiorvalor = matriz[i][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'A soma dos valores pares digitados é {somapares}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha é {maiorvalor}')
