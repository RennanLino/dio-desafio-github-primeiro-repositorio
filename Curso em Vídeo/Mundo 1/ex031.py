d = float(input('Distância da viagem (Km): '))
if d <= 200:
    print('O preço desta viagem será de R$ {}' .format(d * 0.5))
else:
    print('O preço desta viagem será de R$ {}' .format(d * 0.45))
