print('==========CONDIÇõES==========')

v = int(input('Informe a velocidade do carro: '))

if v > 80:
    c = v - 80
    m = c * 7
    
    print('Sua velocidade foi registrada como {}km/h acima do limite! Você receberá um multa no valor de R${}.'.format(c, m))

print('Sua velocidae é de {}km/h. Você está dentro do limite de velocidade!'.format(v))