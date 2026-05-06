print('==========STRINGS==========')

nome = str(input('Insira um nome:')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras.'.format(nome.find(' ')))