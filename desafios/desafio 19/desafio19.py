print('==========Escolhas aleatórias==========')

from random import choice

n1 = str(input('Escolha 1: '))
n2 = str(input('Escolha 2: '))
n3 = str(input('Escolha 3: '))
n4 = str(input('Escolha 4: '))
n5 = str(input('Escolha 5: '))
lista = [n1, n2, n3, n4, n5]

sort = choice(lista)

print('Resultado do sorteio: {}'.format(sort))

