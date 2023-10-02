#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.
km = int(input('Qual a velocidade de carro (km/h)? '))
multa = float((km - 80)*7)
if km > 80:
    print('VOCÊ ESTÁ MULTADO!!!\nSua multa é de R${:.2f}'.format(multa))
else:
    print("ESTÁ DENTRO DO LIMITE DE VELOCIDADE!")