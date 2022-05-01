b = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino',
     'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR',
     'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia', 'América-MG',
'Juventude', 'Grêmio', 'Sport', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {b[:5]}')
print(f'Os 4 ultimos colocados são: {b[-4:]}')
print(f'Em ordem alfabética: {sorted(b)}')
pc = b.index('Chapecoense') + 1
print(f'O Chapecoense está na {pc}ª posição.')