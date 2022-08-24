'''print('=== Caixa Eletrônico ===')
valor = int(input('Valor a ser sacado: R$'))
print('Você receberá:')

total50 = valor // 50
valor = valor - (total50 * 50)
print(f'{total50} cédulas de R$50,00')

total20 = valor // 20
valor = valor - (total20 * 20)
print(f'{total20} cédulas de R$20,00')
total10 = valor // 10
valor = valor - (total10 * 10)
print(f'{total10} cédulas de R$10,00')
total1 = valor // 1
print(f'{total1} cédulas de R$1,00')'''

print('=== Caixa Eletrônico ===')
valor = int(input('Valor a ser sacado: R$'))
print('Você receberá:')
total = valor
totalcedula = 0
cedula = 50

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'{totalcedula} cédulas de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
