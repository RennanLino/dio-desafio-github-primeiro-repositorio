from random import randint
from time import sleep


def sortear(a):
    l = []
    print(f'Sorteando {a} valores da lista:', end=' ')
    for c in range(0, a):
        sleep(0.5)
        x = randint(1, 10)
        l.append(x)
        print(x, end=' ')
    print('Pronto!')
    return l

def somapar(lst):
    s = 0
    for c in lst:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {lst}, temos {s}')


#Programa principal
x = sortear(5)
somapar(x)

