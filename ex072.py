intervalo = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
             'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
             'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero in range(0, 21):
        break
    print('Número inválido.', end=' ')
print(f'Você digitou o número {intervalo[numero]}.')