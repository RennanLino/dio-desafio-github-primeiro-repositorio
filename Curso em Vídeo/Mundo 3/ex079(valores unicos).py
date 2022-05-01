l = []
while True:
    x = float(input('Digite um valor: '))
    if x in l:
        print('Valor duplicado! Não vou adicionar...')
        q = str(input('Quer continuar? [S/N] ')).strip().upper()
        if q not in 'SN':
            print('Codigo inválido.')
            q = str(input('Quer continuar? [S/N] ')).strip().upper()
        elif q == 'N':
            break
    else:
        l.append(x)
        print('Valor adicionado com sucesso...')
        q = str(input('Quer continuar? [S/N] ')).strip().upper()
        if q not in 'SN':
            print('Codigo inválido.')
            q = str(input('Quer continuar? [S/N] ')).strip().upper()
        elif q == 'N':
            break
print(f'Você digitou os valores {sorted(l)}')