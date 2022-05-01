'''from time import sleep
from random import randint
print('Valores sorteados:')
d = {}
for c in range(1, 5):
    r = randint(1, 6)
    sleep(0.5)
    print(f'   O jogador {c} tirou {r}')
    d[f'jogador {c}'] = r
sleep(0.5)
print('Ranking dos jogadores:')
c = 1
for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True):
    sleep(0.5)
    print(f'   {c}° lugar: {k} com {v}')
    c += 1'''
from time import sleep
from random import randint
from operator import itemgetter
print('Valores sorteados:')
d = {}
for c in range(1, 5):
    r = randint(1, 6)
    sleep(0.5)
    print(f'   O jogador {c} tirou {r}')
    d[f'jogador {c}'] = r
sleep(0.5)
print('Ranking dos jogadores:')
ranking = sorted(d.items(), key=itemgetter(1), reverse=True) # itemgetter(0) = organiza pela chave, itemgetter(0) = organiza pelo valor
print(ranking)
for k, v in enumerate(ranking):
    sleep(0.5)
    print(f'   {k+1}° lugar: {v[0]} com {v[1]}')
