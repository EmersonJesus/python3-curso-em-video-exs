##Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em celsius: '))
f = (c*1.8) + 32
print('{}°C são equivalente á {}°F'.format(c, f))