'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.'''

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno é de {area:.2f}m²')


print('Controle de terrenos')
print('-'*40)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
