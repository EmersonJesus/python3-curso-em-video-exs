'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = dict()
partidas = list()
jogadores = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, jogos):
        partidas.append(int(input(f'  - Quantos gols na partida {i}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else: 
            print('ERRO! Responda somente com S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    o = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if o == 999:
        break
    elif o >= len(jogadores):
        print('Digite um valor valido!')
    else: 
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[o]["nome"]}: ')
        for v, k in enumerate(jogadores[o]['gols']):
            print(f'    -Na partida {v+1}, fez {k} gols.')
    print('-'*40)
print('<< ENCERRANDO >>')
