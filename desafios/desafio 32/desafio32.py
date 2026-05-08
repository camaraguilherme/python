print('==========CONDIÇõES==========')

afm = 'É'
neg = 'NÃO'
cores = {'Vermelho': '\033[31m', 
         'Verde': '\033[32m', 
         'Limpar': '\033[m'}

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} {}{}{} BISSEXTO.'.format(ano, cores['Verde'], afm, cores['Limpar']))

else: 
    print('O ano {} {}{}{} é BISSEXTO.'.format(ano, cores['Vermelho'], neg, cores['Limpar']))
