from random import randint
n = randint(1, 5)
print('Tente advinhar que número inteiro de 0 a 5 estou pensando...')
r = int(input('Número: '))
if r == n:
    print('Você acertou! O número que pensei foi {}.' .format(n))
else:
    print('Você errou =/ \nO número que eu pensei foi {}.' .format(n))