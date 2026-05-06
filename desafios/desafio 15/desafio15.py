print('==========Aluguel de Carros==========')

a = int(input('Por quantos dias você alugou o carro?'))
b = float(input('Quantos Km você utilizou o carro?'))

d = a * 60
k = b * 0.15
t = d + k

print('Total de dias: {}.\n Total de Km: {}km.\n Valor do aluguel: R${}.\n Valor da quilometragem: R${}.\n Despesas totais: R${}'.format(a, b, d, k, t))