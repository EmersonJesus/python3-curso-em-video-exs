# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('===================================================\n             EMPRÉSTIMO BANCÁRIO\n===================================================' )
casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos pagar: '))
prest = casa / (anos*12)
if prest <= (sal*0.30):
    print('A prestação mensal será de R${:.2f}!'.format(prest))
else:
    print('Desculpe não podemos aprovar o empréstimo!')