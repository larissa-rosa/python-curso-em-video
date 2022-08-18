largura = float(input('Qual a largura da parede em metros? '))
altura =  float(input('Qual a altura da parede em metros? '))

print('A área da parede é de {:.2f} metros quadrados. São necessários {:.2f} litros de tinta para pintá-la'.format(largura*altura, (largura*altura)/2))
