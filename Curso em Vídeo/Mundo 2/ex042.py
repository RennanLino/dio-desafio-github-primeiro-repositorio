#Analisa tres comprimentos de retas para dizer se podem formar um triangulo. Caso possam, informa o tipo de triangulo
a = float(input('Primeiro comprimento: '))
b = float(input('Segundo comprimento: '))
c = float(input('Terceiro comprimento: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar um triângulo.')
    if a == b == c:
        print('O triângulo formado é equilátero')
    elif a == b != c or a != b == c:
        print('O triangulo formado é Isóceles')
    elif a != b != c:
        print ('O triangulo formado é Escaleno')
else:
    print('As retas não podem formar um triângulo')