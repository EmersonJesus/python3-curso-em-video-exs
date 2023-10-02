# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
c = 0
while c == 0:
    sexo = str(input('Qual seu sexo? [M/F] ')).upper()
    if sexo == 'M':
        c += 1
        print('Você é do sexo Masculino')
    elif sexo == 'F':
        c += 1
        print('Você é do sexo Feminino')
    else:
        print("COMANDO INVALIDO!")
