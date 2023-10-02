def notas(*nts, sit=False):
    lista = dict()
    maior = menor = tot = 0
    lista['total'] = len(nts)
    for i, k in enumerate(nts):
        if i == 0:
            maior = k
            menor = k
        
        if k > maior:
            maior = k
        if menor > k:
            menor = k
            
        tot += k

    lista['maior'] = maior
    lista['menor'] = menor
    lista['media'] = tot / len(nts)
    if sit:
        if (tot/len(nts)) <= 6:
            lista['situação'] = 'RUIM'
        else:
            lista['situação'] = 'BOA'
    return lista
        

if __name__ == '__main__':
    resp = notas(9, 8.5, 7, 6, sit=True)
    print(resp)