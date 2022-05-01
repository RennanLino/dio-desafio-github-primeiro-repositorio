x = (int(input('Digite um valor: ')), int(input('Digite um valor: '))
     , int(input('Digite um valor: ')), int(input('Digite um valor: ')))
if 9 in x:
    print(f'O valor 9 apareceu {x.count(9)}.')
else :
    print('O valor 9 não foi digitado.')
if 3 in x:
    print(f'O valor 3 apareceu primeiro na posição {x.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado')
'''print(f'Os números pares foram: ', end='')
for n in x:
    if n % 2 == 0:
        print(n, end=' ')'''
print('Os números pares foram:', ' '.join((f"{n}" for n in x if n % 2 == 0)))
