def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno de {largura}x{comprimento} é {a} m²')


l = float(input('Largura do terreno em metros: '))
c = float(input('Comprimento do terreno em metros: '))
area(l, c)
