lista = []
exp = str(input('Digite uma expressão matemática: '))
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')

