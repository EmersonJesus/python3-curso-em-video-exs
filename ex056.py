# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.
tot = 0
velho = ''
idadevelho = 0
totidade = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa(F OU M): '.format(c))).strip().upper()
    tot += idade
    if sexo == 'F':
        if idade < 20:
            totidade += 1
    if c == 1:
        if sexo == 'M':
            idadevelho = idade
            velho = nome
    else:
        if idade > idadevelho:
            velho = nome
media = tot/4
print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {}'.format(velho))
print('Tem {} mulheres com menos de 20 anos'.format(totidade))