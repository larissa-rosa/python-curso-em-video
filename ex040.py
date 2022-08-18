nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print('A média do aluno é {}.'.format(media))
if media < 5:
    print('O aluno está reprovado.')
elif media >= 5 and media < 7:
    print(('O aluno está de recuperação.'))
elif media >= 7:
    print('O aluno está aprovado.')