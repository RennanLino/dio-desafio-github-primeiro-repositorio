l = []
lp = []
q = 's'
p = 0
while q != 'N':
    lp.append(str(input('Nome: ')))
    lp.append(float(input('Nota 1: ')))
    lp.append(float(input('Nota 2: ')))
    l.append(lp[:])
    lp.clear()
    q = str(input('Quer continuar? [S/N]')).upper()
    while q not in 'SN':
        print('Código incorreto.')
        q = str(input('Quer continuar? [S/N]')).upper()
print('-='*20)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*28)
for x, b in enumerate(l):
    print(f'{x:<4}{b[0]:<10}{(b[1]+b[2])/2:>8.1f}')
while p != 999:
    print('-' * 28)
    p = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'As notas de {l[p][0]} foram: {l[p][1:]}')
print('FINALIZANDO...')