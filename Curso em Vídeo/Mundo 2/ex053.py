#Indica se uma frase é palindroma
f = str(input('Digite uma frase: ')).strip().upper()
d = f.split()
j = ''.join(d)
c = len(j)
j2 = ''
for a in range(c - 1, -1, -1):
    j2 += j[a]
if j in j2:
    print('A frase é um palíndromo.')
else:
    print('A frase não um palíndromo.')
#Pode-se substituir o for por f[::-1]
print('O inverso de {} é {}.'.format(j, j[::-1]))