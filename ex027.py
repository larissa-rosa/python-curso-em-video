n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #a string vira uma lista
print(nome) #retorna ['Larissa', 'Rosa']
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
