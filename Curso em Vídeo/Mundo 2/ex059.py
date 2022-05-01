#Realiza a operação desejada pelo usuário, entre dois números fornecidos
from time import sleep
m = 0
print('Digite dois números, e depois a operação que deseja realizar de acordo com o menu abaixo.')
while m != 5:
    print('Operações:'
          '\n[ 1 ] - Somar'
          '\n[ 2 ] - Multiplicar'
          '\n[ 3 ] - Retorna o maior valor'
          '\n[ 4 ] - Digitar novos números'
          '\n[ 5 ] - Sair do programa')
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    m = int(input('Operação: '))
    if m == 1:
        s = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
        print('=' * 30)
    elif m == 2:
        x = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, x))
        print('=' * 30)
    elif m == 3:
        l = [n1, n2]
        if n1 == n2:
            print('Os valores digitados são iguais')
        else:
            print('O maior valor digitado foi {}'.format(max(l)))
        print('=' * 30)
    elif m == 4:
        print('Reiniciando ...')
        print('=' * 30)
    elif m == 5:
        break
    else:
        print('Operação inválida. Tente novamente.')
        print('=' * 30)
print('=' * 30)
print('Done.')