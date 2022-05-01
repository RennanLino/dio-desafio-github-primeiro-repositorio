#\033[x;y;zm
#
#x = style
#    0 - sem efeito
#    1 - Bold
#    4 - Underline
#    7 - Negative (inverte cor de fundo com a do texto)
#
#y = text (comeca com 3) ; z = background (comeca com 4)
#    0 - Branco
#    1 - Vermelho
#    2 - Verde
#    3 - Amarelo
#    4 - Azul
#    5 - Magenta
#    6 - Ciano
#    7 - Cinza
#
print('\033[4;30;45mOlá Mundo!\033[m')
nome = 'Child'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'
      .format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'
      .format(cores['amarelo'], nome, cores['limpa']))