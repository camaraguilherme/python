print('==========Conversor de medida==========')

m = float(input('Insira o tamanho (metros):'))

cm = m * 100
mm = m * 1000

print('A medida {}m, equivale a:\nCentímetros: {:.2f}cm \nMilímetros: {:.2f}mm'.format(m, cm, mm))