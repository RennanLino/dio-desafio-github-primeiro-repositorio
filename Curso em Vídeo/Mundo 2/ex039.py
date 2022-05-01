# Programa para informar se alguem precisa fazer o alistamento militar
'''i = int(input('Qual a sua idade? '))
if i < 18:
    print('Você deverá se alistar daqui a {} anos.' .format(18 - i))
elif i == 18:
    print('Já chegou a hora de se alistar')
else:
    print('Voce ja deveria ter se alistado a {} anos' .format(i - 18))'''
#
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
i = atual - nasc
if i < 18:
    print('Você deverá se alistar daqui a {} anos.' .format(18 - i))
    print('Seu alistamento será em {}' .format(18 + nasc))
elif i == 18:
    print('Já chegou a hora de se alistar')
else:
    print('Voce ja deveria ter se alistado a {} anos' .format(i - 18))
    print('Seu alistamento foi em {}' .format(18 + nasc))
