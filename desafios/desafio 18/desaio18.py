print('==========Cálculo de ângulos==========')
from math import radians
from math import sin
from math import cos 
from math import tan
ang = float(input('Insira o ângulo desejado: '))

sen = sin(radians(ang))
co = cos(radians(ang))
tg = tan(radians(ang))

print('O ângulo de {}, tem Seno de {:.2f}'.format(ang, sen))
print('O ângulo de {}, tem Cosseno de {:.2f}'.format(ang, co))
print('O ângulo de {}, tem Tangente de {:.2f}'.format(ang, tg))