print('==========Ordenador==========')

from random import shuffle

n1 = str(input('Escolha 1: '))
n2 = str(input('Escolha 2: '))
n3 = str(input('Escolha 3: '))
n4 = str(input('Escolha 4: '))
n5 = str(input('Escolha 5: '))

lista = [n1, n2, n3, n4, n5]
shuffle(lista)

print('A ordem é: ')
print(lista)
