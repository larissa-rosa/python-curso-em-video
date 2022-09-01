def maior(* numeros):
    cont = maior = 0
    print(f'Valores digitados:', end=' ')
    for num in numeros:
        print(f'{num}', end=' ')
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print()

    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi o {maior}.')
    print('~'*35)


maior(9, 5, 0, 2, -3, 4)
maior(7)
maior()
