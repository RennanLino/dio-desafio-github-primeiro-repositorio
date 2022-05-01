from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
b = radians(a)
print('Os valores de seno, cosseno e tangente para o ângulo {}' .format(a))
print('são respectivamente {:.2f}, {:.2f}, {:.2f}'. format(sin(b), cos(b), tan(b)))
