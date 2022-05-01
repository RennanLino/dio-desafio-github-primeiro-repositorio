n = int(input('Digite um número para ver sua tabuada: '))
print('='*14)
for a in range(1, 11):
    print('{:2} x {:2} = {:2}' .format(n, a, n * a))
print('='*14)