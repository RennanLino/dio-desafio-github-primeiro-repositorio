#Joga pedra, papel e tesoura.
from random import choice
from time import sleep
print('Vamos jogar JOKENPO!\n'
      'Escolha uma das opções abaixo para desputar contra o computador:\n'
      '1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura')
p = int(input('Jogada: '))
e = ['Pedra', 'Papel', 'Tesoura']
c = choice(e)
sleep(1)
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!\n')
sleep(1)
if p == 1 and c == e[0] or p == 2 and c == e[1] or p ==3 and c == e[2]:
      print('O computador também escolheu {}, a disputa foi um {}EMPATE{}!' .format(c, '\033[1m', '\033[m'))
elif p == 1 and c == e[2] or p == 2 and c == e[0] or p == 3 and c == e[2]:
      print('O computador escolheu {}. Parabéns, você {}VENCEU{}!' .format(c, '\033[1;32m', '\033[m'))
elif p == 1 and c == e[1] or p == 2 and  c == e[2] or p == 3 and  c == e[0]:
      print('O computador escolheu {}. Sinto muito, você {}PERDEU{}!' .format(c, '\033[1;31m', '\033[m'))
