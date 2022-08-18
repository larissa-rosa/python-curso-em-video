celsius = float(input('Informe a temperatura em °C: '))
#(0 °C × 9/5) + 32 = 32 °F
fahrenheit = (celsius * 9/5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(celsius, fahrenheit))
