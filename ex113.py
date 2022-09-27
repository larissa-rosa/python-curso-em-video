def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Não é um número inteiro.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return a


def leiaFloat(msg):
    while True:
        try:
            b = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Não é um número real.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return b


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro}, e o valor real digitado foi {real}')
