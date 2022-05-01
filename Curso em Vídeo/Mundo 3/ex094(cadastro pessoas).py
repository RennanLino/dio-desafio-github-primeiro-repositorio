l = []
d = {}
s = 0
while True:
    d['nome'] = str(input('Nome: ')).title()
    d['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if d['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        d['sexo'] = str(input('Sexo [M/F]: ')).upper()
    d['idade'] = int(input('Idade: '))
    s += d['idade']
    l.append(d.copy())
    d.clear()
    q = str(input('Quer continuar? [S/N] ')).upper()
    if q not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        q = str(input('Quer continuar? [S/N] ')).upper()
    if q == 'N':
        break
print('-='*30)
print(f'A) Ao todos temos {len(l)} pessoas cadastradas.')
print(f'B) A média de idade é de {s / len(l)} anos.')
print(f'C) As Mulheres cadastradas foram: ', end='')
for c in l:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for c in l:
    if c['idade'] > s / len(l):
        for k, v in c.items():
            print(f'{k} = {v}', end=': ')
        print()
print('<< ENCERRADO >>')