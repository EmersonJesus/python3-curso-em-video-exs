'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números 
e vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando os valores... ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('PRONTO!')
    soma(lista)


def soma(lista):
    spar = 0
    for i in lista:
        if i % 2 == 0:
            spar += i
    print(f'Somando os valores pares de {lista}, temos {spar}')


numeros = []
sorteia(numeros)