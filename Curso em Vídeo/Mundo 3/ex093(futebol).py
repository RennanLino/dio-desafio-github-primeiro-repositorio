d = {}
gols = []
d['nome'] = str(input('Nome do Jogador: '))
x = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(1, x + 1):
    g = int(input(f'  Quantos gols na partida {c}? '))
    gols.append(g)
d['gols'] = gols[:]
d['total'] = sum(gols)
print('-='*30)
print(d)
print('-='*30)
for k, v in d.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {d["nome"]} jogou {x} partidas.')
for v, c in enumerate(gols):
    print(f'  => Na partida {v + 1}, fez {c} gols.')
print(f'Foi um total de {d["total"]} gols.')
