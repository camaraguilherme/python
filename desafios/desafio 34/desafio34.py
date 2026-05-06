print('==========CONDIÇõES==========')

sa = float(input('Insira o salário do funcionário: '))

if sa > 1250:
    b = sa * 10 / 100
    x = sa + b
    print('O novo salário do funcionário será de R${}.'.format(x))

else:
    c = sa * 15 / 100
    y = sa + c
    print('O novo salário do funcionário será de R${}.'.format(y))


