# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('INICIAR CONTAGEM REGRESSIVA....')
sleep(0.5)
for c in range(10, 0, -1):
    print('{}!'.format(c))
    sleep(0.5)
print('BUM! BUM! POOW!')