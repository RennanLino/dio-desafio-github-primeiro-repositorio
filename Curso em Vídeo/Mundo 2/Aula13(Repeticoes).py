for a in range(0, 5):
    print(a)
print('---')
for b in range(4, 0, -1):
    print(b)
#Conta de 0 até o número informado
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
#Faz somatorio de 4 números
s = 0
for d in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # Igual a (s = s + n)
print('O somatório dos valores foi {}' .format(s))
