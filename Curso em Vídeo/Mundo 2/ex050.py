#Mostra a soma apenas dos números pares informados
s = 0
for a in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares informados foi {}' .format(s))