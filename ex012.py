##Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Digite o valor do produto: '))
d = p - (p*0.05)
print('O valor do produto com 5% de desconto é {:.2f}'.format(d))