print('==========STRINGS==========')

frase = str(input('Escreva uma frase: ')).strip().lower()

print('A letra A aparece {} em sua frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('a')+1))
      