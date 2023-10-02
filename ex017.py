##Faça um programa que leia o comprimento do cateto oposto e do cateto adejacente de 
# um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
op = int(input('Digite o comprimento do cateto oposto: '))
adj = int(input('Digite o comrprimento do cateto adejacente: '))
print('O comprimento da hipotenusa é {}'.format(hypot(op, adj)))

## Sem a biblioteca hypot
## h = sqrt((op**2)+(adj**2))
## print(h)