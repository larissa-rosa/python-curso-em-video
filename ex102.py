def fatorial(num, show=False):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    if show:
        print(f'{num}! = {num}', end='')
        for c in range(num-1, 0, -1):
            print(f' x ', end='')
            print(f'{c}', end='')
        print(f' = ', end='')
    else:
        print(f'Fatorial de {num} = ', end='')
    return fat


print(fatorial(5, True))

