t = float(input('Quantos dias alugados? '))
d = float(input('Quantos Km rodados? '))
T = t * 60 + d * 0.15
print('O total a pagar é de R$ {:.2f}' .format(T))
