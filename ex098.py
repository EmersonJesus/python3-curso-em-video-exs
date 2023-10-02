'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada '''

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(1)
        print('FIM!')
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
            sleep(1)
        print('FIM!')

print('-' * 35)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('-' * 35)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('-' * 35)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print(f'Contagem de {i} até {f} de {+p} em {+p}')
contador(i, f, p)
