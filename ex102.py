def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


if __name__ == '__main__':
    print('-'*40)
    n = int(input('Digite um número: '))
    print(fatorial(n, show=True))