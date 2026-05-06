print('==========Aumento de salário==========')

s = float(input('insira o valor do seu salário:'))

a = s * 15/100
ns = s + a

print('Párabens! Seu salário de R${} aumentou em R${}, agr seu novo salário será de {}.'.format(s, a, ns))
