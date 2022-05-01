#Mostra o fatorial do número informado
n = float(input('Digite um número: '))
c = n
f = n
while c != 1:
    c -= 1
    f *= c
print('O fatorial de {} é igual a {}'.format(n, f))
