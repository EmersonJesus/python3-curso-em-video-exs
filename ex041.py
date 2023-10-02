# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
print('========================\nCONFEDERAÇÃO NACIONAL DE NATAÇÃO\n')
ano = int(input('Que ano o atleta nasceu: '))
if ano > 2023 or ano <= 0:
    print('ANO INVALIDO!')
else:
    idade = 2023 - ano 
    if idade <= 9:
        print('ATLETA MIRIM')
    elif idade > 9 and idade <= 14:
        print('ATLETA INFANTIL')
    elif idade > 14 and idade <= 19:
        print('ATLETA JÚNIOR')
    elif idade > 19 and idade <= 25:
        print('ATLETA SENIOR')
    elif idade > 25:
        print('ATLETA MASTER')