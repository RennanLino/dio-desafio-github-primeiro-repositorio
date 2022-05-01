#Mostra os 10 primeiros termos de uma PA a partir do primeiro termo e a razão.
n = float(input('Primeiro termo: '))
r = int(input('Razão: '))
t = 0
pa = n
x = 1
while t != x + 9:
    while t != x + 9:
        print(pa, end=' | ')
        pa += r
        t += 1
    x += int(input('\nDeseja ver mais quantos termos? '))
print('\nDone.')