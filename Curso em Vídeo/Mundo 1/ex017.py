'''b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))
from math import pow, sqrt
a = sqrt(pow(b, 2) + pow(c, 2))
print('A hipotenusa deste triângulo retangulo é {}' .format(a))'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('Ahipotenusa vai medir {:.2f}' .format(hi))