#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.  
# B) Uma listagem com as pessoas mais pesadas.                                                                                                   
# C) Uma listagem com as pessoas mais leves.
pessoa = list()
grupo = list()
pesadas = list()
leves = list()
op = ''
tot = 0
while True:
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(float(input('Digite o peso dessa pessoa: ')))
    if pessoa[1] >= 100:
        pesadas.append(pessoa[:])
    elif pessoa[1] <= 70:
        leves.append(pessoa[:])
    grupo.append(pessoa[:])
    pessoa.clear()
    tot += 1
    op = str(input('Deseja continuar? [S/N] '))
    if op in 'nN':
        break
print(f'Foram cadastras {tot} pessoas no total!')
print(f'As que pesam 70kg ou menos: {leves}')
print(f'As que pesam 100kg ou mais: {pesadas}')
