from ex109 import moedas

n = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(n)} é {moedas.metade(n=n, f=True)}')
print(f'O dobro de {moedas.moeda(n)} é {moedas.dobro(n=n, f=True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(n=n, f=True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(n=n, f=True)}')