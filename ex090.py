'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Nota do aluno {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = "Aprovado"
elif aluno ['media'] <= 5:
    aluno['situação'] = "Reprovado"
else:
    aluno['situação'] = "Em Recuperação"
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
