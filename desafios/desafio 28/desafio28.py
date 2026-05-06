print('==========CONDIÇõES==========')

from random import randint
from time import sleep

pc = randint(0, 5)

print('-=-' * 20)
print('Tente me vencer adivinhando o número que eu pensei')
print('-=-' * 20)

player = int(input('Escolha um número de 0 a 5: '))

print('Pensando...')
sleep(2.5)

if player == pc:
    print('DROGA! o número é {}. Você me venceu!'.format(pc))
else:
    print('HAHAHAHAHA! O número era {} e você disse {}. EU GANHEI!'.format(pc, player))
