print('==========CONDIÇõES==========')

n = int(input('Informe um número: '))
res = n % 2

if res == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O n úmero {} é ÍMPAR!'.format(n))