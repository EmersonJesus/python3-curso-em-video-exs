# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos
id = totid = homem = mulher20 = 0
sexo = op = ''
while True:
    print('-'*22)
    print('  CADASTRE UMA PESSOA')
    print('-'*22)
    id = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if id > 18:
        totid += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if id < 20:
            mulher20 += 1
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totid}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
