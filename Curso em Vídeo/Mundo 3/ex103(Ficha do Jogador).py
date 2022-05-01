def gols(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


#Programa principal
a = str(input('Nome do Jogador: '))
b = str(input('Número de Gols: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    gols(b=b)
else:
    gols(a, b)