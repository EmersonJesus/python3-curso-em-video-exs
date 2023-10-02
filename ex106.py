def ajuda(fun):
    print(f'Acessando o manual do comando {fun}')
    print(help(fun))

fun = ''
while True:
    print('~'*25)
    print(' SISTEMA DE AJUDA PyHELP')
    print('~'*25)
    fun = str(input('Função ou Biblioteca > ')).strip()
    if fun.upper() == 'FIM':
        break
    else:
        ajuda(fun)
        
        
print('~'*10)
print(' ATÉ LOGO')
print('~'*10)