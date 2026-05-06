print('==========CONDIÇõES==========')

l1 = int(input('Insira o primeiro lado: '))
l2 = int(input('Insira o segundo lado: '))
l3 = int(input('Insira o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados {}, {}, {} podem formar um triângulo.'.format(l1, l2, l3))
else:
    print('Os lados {}, {}, {} NÃO podem formar um triângulo.'.format(l1, l2, l3))