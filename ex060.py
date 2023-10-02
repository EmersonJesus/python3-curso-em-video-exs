# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um valor para ver seu fatorial: '))
c = 0
fat = n
while c == 0:
    for i in range(n, 0, -1):
        print('!{}'.format(n), end='')
        n -= 1     
        if n > 0 :
            print(end=' x ' )       
            fat *= n
    print(end=' = ')
    print(fat)
    c += 1