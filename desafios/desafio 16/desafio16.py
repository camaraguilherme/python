print('==========Somente o número inteiro==========')

from math import trunc

a = float(input('Insira um número com casas após o ponto:'))

print('O valor difitado foi {} e a sua porção inteira é {}'.format(a, trunc(a)))