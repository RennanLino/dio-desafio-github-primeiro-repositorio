#Mostra os n primeiros elementos de uma sequencia de fibonacci
n = int(input('Quantos termos da sequencia de Fibonacci: '))
t = 0
f1 = 1
f2 = 0
print('0', end=' | ')
while t != n:
    f = f1 + f2
    print(f, end=' | ')
    f2 = f1
    f1 = f
    t +=1
