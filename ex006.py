##Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

x = int(input('Digite um número: '))
d = x*2
t = x*3
r2 = x**(1/2)
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {}'.format(x, d, x, t, x, r2))