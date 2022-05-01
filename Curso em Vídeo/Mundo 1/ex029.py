from math import trunc
v = float(input('Velocidade do carro (km/h): '))
if v > 80:
    print('A velocidade está acima da permitida Toreto!\nVocê foi multado.')
    print('Valor da multa: R${}' .format((trunc(v) - 80) * 7))
else:
    print('Muito bem, sem multa hoje.')