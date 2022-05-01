'''a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
# Maior número
if a - b >= 0 and a - c >= 0:
    print('{} é o maior número' .format(a))
if b - a >= 0 and b - c >= 0:
    print('{} é o maior número' .format(b))
if c - a >= 0 and c - b >= 0:
    print('{} é o maior número' .format(c))
# Menor número
if a - b <= 0 and a - c <= 0:
    print('{} é o menor número' .format(a))
if b - a <= 0 and b - c <= 0:
    print('{} é o menor número' .format(b))
if c - a <= 0 and c - b <= 0:
    print('{} é o menor número' .format(c))'''
#
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
print('O maior entre os três números é {}' .format(max(a, b, c)))
print('O menor entre os três números é {}' .format(min(a, b, c)))
#
'''a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
# Maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{} é o maior número' .format(maior))
# Menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('{} é o menor número' .format(menor))'''