#Mostra maior e menos valores digitados e suas respectivas posições na lista
a = []
for c in range(1, 6):
    x = float(input(f'Digite um valor para a posição {c}: '))
    a.append(x)
print(f'Você digitou os valores {a}')
'''print(f'O maior valor foi {max(a)} e suas posições na lista foram: ', end='')
c = 0
for b in a:
    c += 1
    if b == max(a):
        print(f'{c} ', end='')
print(f'\nO menor valor foi {min(a)} e suas posições na lista foram: ', end='')
c = 0
for b in a:
    c += 1
    if b == min(a):
        print(f'{c} ', end='')'''
print(f'O maior valor foi {max(a)} nas posições: ', end='')
for i, v in enumerate(a):
    if v == max(a):
        print(f'{i + 1}...', end='')
print(f'\nO menor valor digitado foi {min(a)} nas posições: ', end='')
for i, v in enumerate(a):
    if v== min(a):
        print(f'{i + 1}...', end='')
