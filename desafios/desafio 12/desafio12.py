print('==========Desconto==========')

v = float(input('insira o valor do produto selecionado:'))

d = v * 5/100
nv = v - d

print('O produto selecionado custava {}, porém teve um desconto de {} e agora passa a custar {}'.format(v, d, nv))
