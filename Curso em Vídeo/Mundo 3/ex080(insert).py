'''l = []
for c in range(1, 6):
    x = float(input('Digite um valor: '))
    if c == 1:
        maior = x
        l.append(x)
        print('Adicionado ao final da lista...')
    elif x > maior:
        maior = x
        l.append(x)
        print(f'Adicionado ao final da lista...')
    else:
        for v, b in enumerate(l):
            if x < b:
                l.insert(v, x)
                print(f'Adicionado a posição {v} na lista...')
                break
print(f'Os valores digitados em ordem foram {l}')'''
l = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(l):
            if n <= lista[pos]
                l.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {l}')