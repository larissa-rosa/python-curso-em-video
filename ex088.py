from random import randint
numeros = []
sorteados = []
print('='*20)
print(f'{"MEGA SENA":^20}')
print('='*20)
jogos = int(input('Quantos jogos você deseja sortear? '))
for c in range(0, jogos):
    cont = 0
    while True:
           n = randint(1, 60)
           if n not in numeros:
               numeros.append(n)
               cont += 1
           if cont >= 6:
               break
    numeros.sort()
    sorteados.append(numeros[:])
    numeros.clear()
for i, l in enumerate(sorteados):
    print(f'Jogo {i+1}: {l}')


