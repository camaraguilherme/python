print('==========Conversor de dinheiro==========')

r = float(input('Insira quantos reais você deseja converter:'))

d = r / 5.01

print('Com o valor de R${}, você obteve US${:.2f}'.format(r, d))