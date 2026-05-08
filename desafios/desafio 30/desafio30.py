print('==========CONDIÇõES==========')

afm = 'PAR'
neg = 'ÍMPAR'
cores = {'Vermelho': '\033[31m', 
         'Verde': '\033[32m', 
         'Limpar': '\033[m'}

n = int(input('Informe um número: '))
res = n % 2

if res == 0:
    print('O número {} é {}{}{}!'.format(n, cores['Verde'], afm, cores['Limpar']))
else:
    print('O n úmero {} é {}{}{}!'.format(n, cores['Vermelho'], neg, cores['Limpar']))