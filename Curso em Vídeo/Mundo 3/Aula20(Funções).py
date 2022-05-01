#Aula 20
def soma(a, b):
    s = a + b
    print(s)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


def dobra(lst):
    for c in range(0, len(lst)):
        lst[c] *= 2


def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


 #Programa principal
soma(4, 5)
soma(8, 9)
#
contador(2, 1, 7)
contador(4, 4, 7, 6, 2)
#
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
#
soma2(5, 2)
soma2(2, 9, 4)
print('-=' * 20)

#Aula 21
help(print)


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


help(contador)


def somar(a, b, c=0): #Se nao for inserido o parametro c, ele toma o valor de 0
    s = a + b +c
    return s


def teste(b):
    global a #valor de 'a' passa de escopo local para global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

 #Programa Principal
r1 = somar(3, 2)
r2 = somar(2, 5, 6)
print(f'Os Resultados foram {r1} e {r2}')

a = 5
teste(a)
print(f'A fora vale {a}')
print('-=' * 20)

#Aula 21 - Prática


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


 #Programa principal
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)
print(f'Os resultados foram {f1}, {f2} e {f3}')

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
