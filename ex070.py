# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
produto = op = nomebarato = ''
preço = barato = mil = tot = 0
while True:
    print('-'*24)
    print('   LOJA SUPER BARATÃO')
    print('-'*24)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    if barato == 0:
        barato = preço
        nomebarato = produto
    else :
        if barato < preço:
            barato = preço
            nomebarato = produto
    tot += preço
    if preço > 1000:
        mil += 1
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')