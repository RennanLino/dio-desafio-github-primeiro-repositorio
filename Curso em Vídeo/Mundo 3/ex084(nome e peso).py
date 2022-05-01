dados = []
pessoas = []
tot = 0
while True:
    n = str(input('Nome: ')).upper()
    p = int(input('Peso: '))
    dados.append(n)
    dados.append(p)
    pessoas.append(dados[:])
    dados.clear()
    tot += 1
    q = str(input('Deseja continuar? [S/N] ')).upper()
    while q not in 'SN':
        print('Código inválido.')
        q = str(input('Deseja continuar? [S/N] ')).upper()
    if q == 'N':
        break
    if tot == 1:
        maior = p
        menor = p
    elif p > maior:
        maior = p
    elif p < menor:
        menor = p
print('-=' * 20)
print(f'Ao todo, você cadastrou {tot} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for v, c in enumerate(pessoas):
    if c[1] == maior:
        print(f'{c[0].title()} ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for v, c in enumerate(pessoas):
    if c[1] == menor:
        print(f'{c[0].title()} ', end='')
