s = str(input('Qual o sexo da pessoa? [F/M] ')).upper().strip()[0]

while s not in 'FfMm':
    s = str(input('Valor inválido. Digite o sexo da pessoa: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(s))
