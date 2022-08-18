"""
programa para ler o nome completo de uma pessoa e mostrar tudo em maiúsculas, tudo em minúsculas, quantas letras
sem considerar espaços, quantas letras tem o primeiro nome
"""

nome = input('Digite seu nome completo: ').strip()

print('Nome em maiúsculas: ', nome.upper())
print('Nome em minúsculas: ', nome.lower())
print('Número de letras do nome + sobrenome: ', len(nome) - nome.count(' '))
print('Número de letras do nome: ', nome.find(' '))