print('==========Calculo de área==========')

h = float(input('Insira a altura da parede (em metros):'))
w = float(input('Insira a largura da parede (em metros):'))

area = h * w 

tinta = area / 2

print('Para pintar a parede de área {}m², você irá precisar de {} litros de tinta.'.format(area, tinta))