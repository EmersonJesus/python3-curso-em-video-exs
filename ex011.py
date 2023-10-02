## Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta -
## necessaria para pinta-lá, sabendo que cada litro de tinta pinta um área de 2m²

l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
ar = l*a
t = ar/2
print('A área total da parede é {:.2f}m² \nVocê irá precisar de {:.2f}l de tinta'.format(ar, t))