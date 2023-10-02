from ex107 import moedas

n = float(input('Digite o preço: '))
print(f'A metade de {n:.2f} é {moedas.metade(n)}')
print(f'O dobro de {n:.2f} é {moedas.dobro(n)}')
print(f'Aumentando 10%, temos {moedas.aumentar(n, 10):.2f}')
print(f'Reduzindo 13%, temos {moedas.diminuir(n, 13):.2f}')