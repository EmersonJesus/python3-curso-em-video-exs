# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
# ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('ALISTAMENTO MILITAR\n==============================')
ano = int(input('Digite o ano que você nasceu: '))
idade = 2023 - ano
if idade == 18:
    print('Você está na idade de se alistar!')
elif idade > 18:
    print('Você já passou da idade de se alistar!')
    print('Você passou {} anos do prazo'.format(idade-18))
else:
    print("Você ainda não tem idade para se alistar!")
    print('Ainda faltam {} anos para se alistar'.format(18-idade))