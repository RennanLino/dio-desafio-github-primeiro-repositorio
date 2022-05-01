from random import randint
from time import sleep


def maior(*num):
    tam = len(num)
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in range(0, tam):
        print(num[c], end=' ')
        sleep(0.5)
    print(f'Foram informados {tam} valores ao todo.')
    if tam != 0:
        print(f'O maior valor informado foi {max(num)}')
    else:
        print(f'O maior valor informado foi 0')

#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()