def aumentar(n=0.0, juros=1, f = False):
    res = (n + (n*(juros/100)))
    return res if f is False else moeda(res)


def diminuir(n=0.0, juros=1, f = False):
    res = (n - (n*(juros/100)))
    return res if f is False else moeda(res)


def dobro(n=0.0, f = False):
    res = n * 2
    return res if f is False else moeda(res)


def metade(n=0.0, f = False):
    res = n / 2
    return res if f is False else moeda(res)


def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n = 0.0, j1 = 0, j2 = 0):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{j1}% de aumento: \t{aumentar(n, j1, True)}')
    print(f'{j2}% de redução: \t{diminuir(n, j2, True)}')
    print('-'*40)