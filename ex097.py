def escreva(texto):
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))


txt = str(input('Digite um texto: '))
escreva(txt)
