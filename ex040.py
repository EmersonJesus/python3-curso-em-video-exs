# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1+nota2)/2
if m < 5.0:
    print('Sua media foi {:.1f}, você foi REPROVADO!'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {:.1f}, vocè está em RECUPERAÇÃO!'.format(m))
elif m >= 7.0:
    print('Sua média foi {:.1f}, você foi APROVADO!'.format(m))