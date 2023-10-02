'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['anodenascimento'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = 2023 - pessoa['anodenascimento']
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = (pessoa['contratação']-pessoa['anodenascimento']) + 40
del pessoa['anodenascimento']
for v, k in pessoa.items():
    print(f'- {v} tem o valor {k}')
