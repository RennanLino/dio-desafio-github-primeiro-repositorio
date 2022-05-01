l = []
pares = []
impares = []
while True:
    x = float(input('Digite um valor: '))
    l.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
    q = str(input('Deseja continuar? [S/N]')).upper()
    while q not in 'SN':
        print('Código inválido.')
        q = str(input('Deseja continuar? [S/N]')).upper()
    if q == 'N':
        break
print(f'Os valores digitados em ordem foram: {sorted(l)}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')