#Mostra os 10 primeiros termos de uma PA a partir do primeiro termo e a razão.
n = float(input('Primeiro termo: '))
r = float(input('Razão: '))
t = 0
pa = n
while t != 10:
    print(pa, end=' | ')
    pa += r
    t += 1
print('\nDone.')
