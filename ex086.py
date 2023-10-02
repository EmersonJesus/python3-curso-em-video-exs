# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[[],[],[]], [[],[],[]], [[],[],[]]]
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].insert(y, (input(f'Digite o valor da posição ({x}, {y}): ')))
print('=-'*30)
print(f"""{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}
----------
{matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}
----------
{matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}""")