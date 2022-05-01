m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = 0
s3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        x = int(input(f'Digite um valor para a porsição [{l};{c}]: '))
        m[l][c] = x
        if x % 2 == 0:
            s += x
        if c == 2:
            s3 += x
print('='*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    print()
print('='*40)
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {max(m[1])}')
