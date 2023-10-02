## Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
## Considere o dolar $3,27

din = float(input('Quantos reais você tem na carteira: R$'))
dol = din/3.27
print("Com R${} você poderia comprar US${:.2f}".format(din, dol))