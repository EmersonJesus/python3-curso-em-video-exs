def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg).strip()
        try:
            valor = int(n)
            break
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Entrada interrompida pelo usuario')
            return 0
    return valor


def leiaFloat(msg):
    valor = 0
    while True:
        n = input(msg).strip().replace(',', '.')
        try:
            valor = float(n)
            break
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Entrada interrompida pelo usuario')
            return 0
    return valor


if __name__ == '__main__':
    n = leiaInt('Digite um número inteiro: ')
    f = leiaFloat('Digite um número real: ')
    print(f'O valor inteiro digitado foi {n} e o valor real foi {f}')