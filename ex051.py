# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
print('=======================\n10 TERMOS DE UMA PA\n=======================')
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pri + (10-1) * raz
for c in range(pri, dec + raz, raz):
    print('{}'.format(c), end=' - ')
print('ACABOU')