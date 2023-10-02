##Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maiúsculas e minúsculas.
## Quantas letras ao todo (sem considerar espaços).
##Quantas letras tem o primeiro nome.
nome = str(input("Digite seu nome: "))
nome = nome.strip()
print(nome.upper())
print(nome.lower())
primeironome = nome.split()
nome = ''.join(primeironome)
print('Seu nome completo tem {} letras'.format(len(nome)))
print('Seu primeiro nome tem {} letras'.format(len(primeironome[0])))
