def aumentar(n=0.0, juros=1, f = False):
    res = (n + (n*(juros/100)))
    return res if f is False else res


def diminuir(n=0.0, juros=1, f = False):
    res = (n - (n*(juros/100)))
    return res if f is False else res

def dobro(n=0.0, f = False):
    res = n * 2
    return res if f is False else res

def metade(n=0.0, f = False):
    res = n / 2
    return res if f is False else res


def moeda(n, moeda = 'R$'):
    return f'{moeda}{n}'.replace('.', ',')