# Aprimore o desafio anterior, mostrando no final:         
# A) A soma de todos os valores pares digitados.  
# B) A soma dos valores da terceira coluna.   
# C) O maior valor da segunda linha.
num = 0
matriz = [[[],[],[]], [[],[],[]], [[],[],[]]]
par = terceira = maior = 0
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite o valor da posição ({x}, {y}): '))
        matriz[x].insert(y, num)
        if num % 2 == 0 :
            par += num
        if y == 2:
            terceira += num
        if x == 1:
            if y == 0:
                maior = num
            else:
                if num > maior:
                    maior = num
print('=-'*30)
print(f"""{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}
----------
{matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}
----------
{matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}""")
print('=-'*30)
print(f'A soma de todos os valores pares digitados é {par}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
print('=-'*30)