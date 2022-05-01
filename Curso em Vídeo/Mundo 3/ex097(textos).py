def lin(txt):
    a = len(txt)
    print('~' *(a + 4))
    print(f'{txt:^{a + 4}}')
    print('~' *(a + 4))


#
lin('Curso de Python no Youtube')
lin('CeV')