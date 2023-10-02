# Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for c in range(1, 7):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        s += x
print('A soma dos valores pares é {}'.format(s))