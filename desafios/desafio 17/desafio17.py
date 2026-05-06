print('==========Cálculo da Hipotenusa==========')

from math import hypot

co = float(input('Insira o valor do Cateto Oposto: '))
ca = float(input('Insira o valor do Cateto Adjacente: '))
hi = hypot(co, ca)

print('O valor da hipotenusa é: {:.2f}'.format(hi))