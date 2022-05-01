#Calcula a soma entre todos os numeros impares multiplos de 3 entre 1 e 500
s = 0
for a in range(0, 501, 3):
    s += a
print(s)