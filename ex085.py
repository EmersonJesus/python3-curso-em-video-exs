# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
num = list()
pares = list()
impares = list()
for c in range(0, 7):
    num.append(int(input(f'Digite o {c+1}º valor: ')))
    if num[0] % 2 == 0:
        pares.append(num[:])
    else:
        impares.append(num[:])
    num.clear()
pares.sort()
impares.sort()
print('-='*30)
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')
