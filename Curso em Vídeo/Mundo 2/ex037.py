# Programa para converter um numero para as bases: binária, octal ou hexadecimal
n = int(input('Digite um número: '))
print('Escolha para que base convter o número, digitando:\n'
      '1 para binário\n'
      '2 para octal\n'
      '3 para hexadecimal')
d = int(input('Base: '))
b = bin(n)
o = oct(n)
h = hex(n)
if d == 1:
      print('O numero {} em binário é {}' .format(n, b[2:]))
elif d == 2:
      print('O numero {} em binário é {}'.format(n, o[2:]))
elif d == 3:
      print('O numero {} em binário é {}'.format(n, h[2:]))
else:
      print('Você é burro?\n'
            'Eu disse 1, 2 ou 3.')