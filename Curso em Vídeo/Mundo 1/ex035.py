a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')