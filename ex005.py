##Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
  
x = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(x, (x-1), (x+1)))