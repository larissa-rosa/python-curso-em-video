aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print(aluno)

for k, v in aluno.items():
    print(f'* {k} é igual a {v}')