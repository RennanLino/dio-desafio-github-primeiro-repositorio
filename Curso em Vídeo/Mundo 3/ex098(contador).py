from time import sleep


def contador(a, b, c):
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a >= b:
        while a >= b:
            print(a, end=' ')
            sleep(0.5)
            a -= abs(c)
    elif b >= a:
        while b >= a:
            print(a, end=' ')
            sleep(0.5)
            a += abs(c)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim:    '))
c = int(input('Passo:  '))
contador(a, b, c)
