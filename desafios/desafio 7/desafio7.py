print('==========Insira o nome da matéria e suas 5 notas abaixo para saber sua média==========')

mat = input('Insira o nome da matéria:\n')
n1 = float(input('Insira sua primeira nota:\n'))
n2 = float(input('Insira sua segunda nota:\n'))
n3 = float(input('Insira sua terceira nota:\n'))
n4 = float(input('Insira sua quarta nota:\n'))
n5 = float(input('Insira sua quinta nota:\n'))

m = (n1 + n2 + n3 + n4 + n5)/5

print('Sua média na matéria {} é {:.2f}.'.format(mat, m))