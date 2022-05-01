#Mosta o maior e o menos peso, entre 5 pessoas
a = []
for b in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa'.format(b)))
    a.append(p)
print('O maior peso foi {:.2f} Kg' .format(max(a)))
print('O menor peso foi {:.2f} Kg' .format(min(a)))
