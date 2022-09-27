from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('Opção inválida')



