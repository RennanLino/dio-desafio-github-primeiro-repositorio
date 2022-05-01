#Lê números repetidamente, e mostra a soma no final. O código de parada é 999
s = 0
t = 0
x = int(input('Digite um número: '))
while x != 999:
    s += x
    t += 1
    x = int(input('Digite um número: '))
print('Um total de {} números foram digitados, e a soma deles foi {}.'.format(t, s))