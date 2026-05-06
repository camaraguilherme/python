print('==========CONDIÇõES==========')

v = float(input('Escreva a distância da viagem em KM: '))

if v > 200: 
    p1 = v * 0.45
    print('Sua passagem custará {}.'.format(p1))

else: 
    p2 = v * 0.5
    print('Sua passagem custará {}.'.format(p2))