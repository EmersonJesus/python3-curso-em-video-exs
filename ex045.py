#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada: '))
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print("JOGADA INVALIDA!")
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print("JOGADA INVALIDA!")