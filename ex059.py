# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
c = 0
while c == 0:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('R: '))
    if op == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('O produto entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os valores são iguais!')
    elif op == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif op == 5: 
        c += 1
    else:
        print("COMANDO INVALIDO!")