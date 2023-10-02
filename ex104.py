def leiaInt(msg):
    print('-' * 30)
    valor = 0
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return valor

if __name__ == '__main__':
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o número {n}')