'''t = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
     'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
     'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)
for n in range(0, 18):
     if n == 0 or n % 2 == 0:
          print(f'{t[n]}', 'R$'.rjust((32-len(t[n])), '.'), f'{t[n + 1]}'.rjust(6))
print('-' * 40)'''
t = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
     'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
     'Canetas', 22.3, 'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(t)):
     if pos % 2 == 0:
          print(f'{t[pos]:.<30}', end='')
     else:
          print(f'R${t[pos]:>7.2f}')