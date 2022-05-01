l = []
d = {}
gols = []
while True:
    d['nome'] = str(input('Nome do Jogador: ')).title()
    d['partidas'] = int(input(f'Quantas partidas {d["nome"]} jogou? '))
    s = 0
    for c in range(1, d['partidas'] + 1):
        g = int(input(f'Quantos gols na partida {c}? '))
        s += g
        gols.append(g)
    d['gols'] = gols[:]
    d['total'] = s
    l.append(d.copy())
    d.clear()
    gols.clear()
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if q == 'N':
        break
print('-='*30)
print(f'{"cod":<4}{"Nome":<12}{"Gols":<17}{"Total":>8}')
print('-'*60)
for i, e in enumerate(l):
    print(f'{i:>3} {e["nome"]:<11} {str(e["gols"]):<19} {e["total"]:<8}')
print('-'*60)
while True:
    j = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if j == 999:
        break
    for i, e in enumerate(l):
        if j == i:
            print(F'-- LEVANTAMENTO DO JOGADOR {e["nome"].upper()} --')
            for c in range(1, len(e['gols']) + 1):
                print(f'  No jogo {c} fez {e["gols"][c - 1]} gols.')
    if j > len(l):
        print(f'ERRO! Não existe jogador com código {j}!')
#    try:
#       t = l[j]  #checa se existe o indice 'j' na lista 'l'
#    except IndexError:
#        print(f'ERRO! Não existe jogador com código {j}!')  #se nao existir exibe esta mensagem
    print('-' * 60)
print('<< VOLTE SEMPRE >>')