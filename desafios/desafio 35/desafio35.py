print('==========CONDIÇõES==========')

afm = 'PODEM'
neg = 'NÃO'
cores = {'Vermelho': '\033[31m', 
         'Verde': '\033[32m', 
         'Limpar': '\033[m'}

l1 = int(input('Insira o primeiro lado: '))
l2 = int(input('Insira o segundo lado: '))
l3 = int(input('Insira o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados {}, {}, {} {}{}{} formar um triângulo.'.format(l1, l2, l3, cores['Verde'], afm, cores['Limpar']))
else:
    print('Os lados {}, {}, {} {}{}{} podem formar um triângulo.'.format(l1, l2, l3, cores['Vermelho'], neg, cores['Limpar']))