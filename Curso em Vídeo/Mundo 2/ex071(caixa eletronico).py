#Pergunta valor a ser sacado e informa quantas cedulas serao entregues.
'''print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40)
v = int(input('Qual o valor que quer sacar? R$ '))
c50 = c20 = c10 = c1 = 0
while True:
    if v >= 50:
        v -= 50
        c50 += 1
    elif v >= 20:
        v -= 20
        c20 += 1
    elif v > 10:
        v -= 10
        c10 += 1
    elif v >= 1:
        v -= 1
        c1 += 1
    elif v == 0:
        break
print(f'Total de {c50} cédulas de R$ 50'
      f'\nTotal de {c20} cédulas de R$ 20'
      f'\nTotal de {c10} cédulas de R$ 10'
      f'\nTotal de {c1} cédulas de R$ 1')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''
#
print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40)
valor = int(input('Qual o valor que quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')