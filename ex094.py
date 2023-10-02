'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoa = dict()
pessoas = list()

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        opc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opc in 'SN':
            break
        else:
            ('ERRO! Responda apenas S ou N.')
    if opc == 'N':
        break
print('-=' * 30)
totpessoas = len(pessoas)

totid = 0
for p in pessoas:
    totid += p['idade']
mediaid = totid/totpessoas

mulheres = list()
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])

acimamedia = list()
for p in pessoas:
    if p['idade'] > mediaid:
        acimamedia.append(p)

print(f'A) Foram cadastradas {totpessoas} pessoas.')
print(f'B) A média de idade é de {mediaid:.1f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista das pessoas que estão acima da média: ')
for p in acimamedia:
    for k, v in p.items():
        print(f'    -{k} = {v}', end=' ; ')
    print()
print('<< ENCERRADO >>')