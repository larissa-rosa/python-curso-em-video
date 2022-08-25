tupla = ('Pao', 'Bolo', 'Sonho', 'Croissant', 'Chocolate', 'Torta', 'Pastel')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos as vogais ', end='')
    for letra in c:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')