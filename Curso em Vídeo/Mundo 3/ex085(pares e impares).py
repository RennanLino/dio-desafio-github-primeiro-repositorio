l = [[], []]
for c in range(1, 8):
    x = int(input(f'Digite o {c}° valor: '))
    if x % 2 == 0:
        l[0].append(x)
    else:
        l[1].append(x)
print(f'Os valores pares são: {sorted(l[0])}')
print(f'Os valores ímpares são: {sorted(l[1])}')