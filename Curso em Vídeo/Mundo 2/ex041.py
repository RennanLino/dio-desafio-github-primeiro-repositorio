#Mostra a categoria de natação de uma pessoa a partir da idade
i = int(input('Digite a idade: '))
if i <= 9:
    print('Categoria: {}MIRIM{}' .format('\033[1;34m', '\033[m'))
elif i <= 14:
    print('Categoria: {}INFANTIL{}'.format('\033[1;34m', '\033[m'))
elif i <= 19:
    print('Categoria: {}JUNIOR{}' .format('\033[1;34m', '\033[m'))
elif i <= 25:
    print('Categoria: {}SÊNIOR{}' .format('\033[1;34m', '\033[m'))
else:
    print('Categoria: {}MASTER{}' .format('\033[1;34m', '\033[m'))