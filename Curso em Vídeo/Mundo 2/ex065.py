#Lê vários números inteiros, mostra a média entre eles, quais foram o maior e menos. Pergunta se o usuário deseja continuar
l = []
x = 's'
while x != 'N':
    n = int(input('Digite um número: '))
    l.append(n)
    x = str(input('Deseja adicionar mais números [S/N]? ')).strip().upper()
    while x != 'S' and x != 'N':
        print('Código inválido.')
        x = str(input('Deseja adicionar mais números [S/N]? ')).strip().upper()
print('A média entre os valores digitados foi {}.'.format(sum(l) / len(l)))
print('O maior valor digitado foi {}, e o menor {}.'.format(max(l), min(l)))
