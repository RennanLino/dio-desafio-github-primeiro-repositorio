#Mostra quantas dentre as 7 pessoas ja sao maior de idade a partir do ano de nascimento
from datetime import datetime
a = datetime.today().year
b = 0
for c in range(0, 7):
    i = int(input('Digite o ano de nascimento: '))
    if i <= a - 21:
        b += 1
print('Dentre estas 7 pessoas, {} ja atingiram a maioridade.' .format(b))