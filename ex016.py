##Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor
num = float(input('Digite um número real: '))
print('A forma inteira de {:.1f} é {}'.format(num, floor(num)))