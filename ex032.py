# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Digite um ano (DIGITE 0 PARA VER O ANO ATUAL): '))
if ano%4 == 0:
    if ano == 0:
        print('2023 não é um ano bissexto')
    else:
        print("{} é um ano bissexto".format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
