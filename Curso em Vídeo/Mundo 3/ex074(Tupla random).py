from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
t = (a, b, c, d, e)
print(f'Os valores sorteados foram: {t}'
      f'\nO maior valor foi {max(t)}'
      f'\nO menor valor foi {min(t)}')
