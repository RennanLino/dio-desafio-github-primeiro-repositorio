l = []
while True:
    x = float(input('Digite um valor: '))
    l.append(x)
    q = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if q == 'N':
        break
    while q not in 'SN':
        print('Código inválido.')
        q = str(input('Deseja continuar? [S/N] ')).strip().upper()
print('=' * 40)
print(f'Você digitou {len(l)} elementos.')
l.sort(reverse=True)
print(f'Os valores digitados em ordem são: {l}')
if 5 in l:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi digitado.')