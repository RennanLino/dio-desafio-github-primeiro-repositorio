#Jogo onde o computador 'Pensa' num número. e o jogador tenta adivinhar
from random import randint
print('Estou pensando em um número entre 1 e 10.')
n = int(input('Que número é este? '))
r = randint(1, 10)
t = 1
while n != r:
    t +=1
    if n < r:
        print('{}ERROU!{} O número que pensei é maior que {}. Tente novamente.'.format('\033[1;31m','\033[m', n))
    else:
        print('{}ERROU!{} O número que pensei é menor que {}. Tente novamente.'.format('\033[1;31m','\033[m', n))
    n = int(input('Que número estou pensando? '))
print('{}ACERTOU!{} O número que pensei foi o {}. Parabéns!'
      '\nVocé precisou de {} tentativas para acertar.'.format('\033[1;34m', '\033[m', r, t))
