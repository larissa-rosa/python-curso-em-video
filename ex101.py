def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 16:
        return f'{idade} anos: não vota'
    elif idade < 18 or idade > 65:
        return f'{idade} anos: voto opcional'
    else:
        return f'{idade} anos: voto obrigatório'

nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
