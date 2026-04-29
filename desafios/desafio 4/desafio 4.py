A = str(input('Digite algo:'))

print(type(A))

print('A faz parte do alfabeto?', A.isalpha())
print('A é um número?', A.isnumeric())
print('A tem letras e/ou números?', A.isalnum())
print('A tem espaço?', A.isspace())
print('A tem somente letras maiúsculas?', A.isupper())
print('A tem somente letras minúsculas?', A.islower())
print('A pode ser impresso?', A.isprintable())
