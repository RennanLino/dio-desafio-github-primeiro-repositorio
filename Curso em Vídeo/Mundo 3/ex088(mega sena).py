from random import randint
from time import sleep
l = []
print('-'*40)
a = 'JOGA NA MEGA SENA'
print(f'{a:^40}')
print('-'*40)
n = int(input('Quantos jogos você que eu sorteie? '))
sleep(0.5)
b = f'SORTEANDO {n} JOGOS'
print(f'{b:=^40}')
sleep(1)
for v in range(1, n +1):
    while len(l) != 6:
        x = randint(0, 60)
        if x not in l and x != 0:
            l.append(x)
    sleep(0.25)
    print(f'Jogo n° {v}: {sorted(l)}')
    sleep(0.5)
    l.clear()
sleep(1)
c = 'BOA SORTE !'
print(f'{c:=^40}')
