def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    ok = False
    valor = 0
    while not ok:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'Erro! \"{entrada}\" é um preço inválido!')
    return valor

