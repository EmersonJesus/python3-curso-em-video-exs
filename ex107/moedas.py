def  aumentar(n=0.0, juros=1):
    return float(n + (n*(juros/100)))

def diminuir(n=0.0, juros=1):
    return float(n - (n*(juros/100)))

def dobro(n=0.0):
    return n * 2

def metade(n=0.0):
    return n / 2
