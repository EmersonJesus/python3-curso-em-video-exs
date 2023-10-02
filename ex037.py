# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('=================\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
op = int(input(':'))
num = int(input('Digite o número que quer converter: '))
if op == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA')