def lin(txt):
    print('-'*50)
    print(f'{txt:^50}')
    print('-'*50)


def area(a, b):
    x = a * b
    lin(f'A área de um terreno de {a}x{b} e de {x}m².')


#
lin('Controle de Terrenos')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
