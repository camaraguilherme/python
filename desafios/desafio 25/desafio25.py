print('==========STRINGS==========')

nome = str(input('Escreva seu nome completo: ')).strip().title().split()
n1 = nome[ : ]
print('O nome possui Silva: {}'.format('Silva' in nome))