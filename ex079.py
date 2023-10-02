# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
op = ''
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores: {valores}')
