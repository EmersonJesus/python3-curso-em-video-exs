'''from ex108 '''
import moedas

n = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(n)} é {moedas.moeda(moedas.metade(n))}')
print(f'O dobro de {moedas.moeda(n)} é {moedas.moeda(moedas.dobro(n))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(n, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(n, 13))}')