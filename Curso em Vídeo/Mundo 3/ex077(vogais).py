'''t = ('Nessa', 'aula', 'vamos', 'aprender', 'TUPLAS', 'como', 'utilizar',
'tuplas', 'Python', 'tuplas', 'variaveis', 'compostas', 'permitem',
'armazenar', 'valores', 'mesma', 'estrutura', 'chaves', 'individuais')
for p in t:
    p = p.upper()
    print(f'\nNa palavra {p} temos ', end='')
    for l in p:
        if l == 'A':
            print('a ', end='')
        if l == 'E':
            print('e ', end='')
        if l == 'I':
            print('i ', end='')
        if l == 'O':
            print('o ', end='')
        if l == 'U':
            print('u ', end='')'''
t = ('Nessa', 'aula', 'vamos', 'aprender', 'TUPLAS', 'como', 'utilizar',
'tuplas', 'Python', 'tuplas', 'variaveis', 'compostas', 'permitem',
'armazenar', 'valores', 'mesma', 'estrutura', 'chaves', 'individuais')
for p in t:
    print(f'\nNa palavra {p.title()} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end='')