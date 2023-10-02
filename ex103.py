def ficha(nome="<desconhecido>", gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


if __name__ == '__main__':
    print('-'*40)
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Número de gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        print(ficha(gols=gols))
    else:
        print(ficha(nome, gols))