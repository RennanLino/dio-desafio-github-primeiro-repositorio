m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        x = int(input(f'Digite um valor para a porsição [{l};{c}]: '))
        m[l][c] = x
print('='*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    print()