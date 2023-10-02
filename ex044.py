# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros
print('===================================')
preço = float(input('Digite o valor da compra: '))
print('\nESCOLHA A FORMA DE PAGAMENTO:\n[1] Á VISTA DINHEIRO/CHEQUE\n[2] Á VISTA NO CARTÃO\n[3] EM 2x NO CARTÃO\n[4] EM 3x OU  MAIS NO CARTÃO')
op = int(input(':'))
if op > 4 or op < 1:
    print('ESCOLHA INVALIDA!')
else:
    if op == 1:
        print('VOCÊ ESCOLHEU PAGAR Á VISTA NO DINHEIRO OU CHEQUE')
        print('O VALOR A PAGAR É {:.2f}'.format(preço-(preço*0.10)))
    elif op == 2:
        print('VOCÊ ESCOLHEU PAGAR Á VISTA NO CARTÃO')
        print('O VALOR A PAGAR É {:.2f}'.format(preço-(preço*0.05)))
    elif op == 3:
        print('VOCÊ ESCOLHEU PAGAR PARCELADO EM 2x NO CARTÃO')
        print('O VALOR A PAGAR SÃO DUAS PARCELAS DE {:.2f}'.format(preço/2))
    elif op == 4:
        print('VOCÊ ESCOLHEU PAGAR PARCELADO EM 3x OU MAIS NO CARTÃO')
        print('O VALOR A PAGAR É {:.2f} QUE SERÁ PARCELADO EM 3x OU MAIS'.format(preço+(preço*0.20)))