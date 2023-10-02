from utilidadesCeV import moeda

def leiadinheiro(msg):
    while True:
        preco = str(input(msg)).replace(',', '.').strip()
        if preco.isalpha() or preco == '':
            print(f'ERRO, "{preco}" não é um valor válido!')
        else:    
            break
        
    return float(preco)