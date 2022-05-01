#Mostra os 10 primeiros termos de uma progressão aritmética
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos desta PA são:')
for a in range(n, n + r * 10, r):
    print(a, end=' ')
