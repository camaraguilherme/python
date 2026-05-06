print('==========CONDIÇõES==========')

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

#Verificando o menor número 
menor = a
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c

print('O menor número é: {}.'.format(menor))

#Verificando o maior número 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número é: {}.'.format(maior))