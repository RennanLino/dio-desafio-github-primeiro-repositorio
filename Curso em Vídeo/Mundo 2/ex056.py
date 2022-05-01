#Mostra média de idade do grupo, nome do homem mais velho e quantas mulheres têm menos de 20 anos
lmn = [] #Lista com nomes de homens
lmi = [] #Lista com idades de homens
lfn = [] #Lista com nomes de mulheres
lfi = [] #Lista com idades de mulheres
for a in range(1, 5):
    print('=' * 12)
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    g = str(input('Sexo (M/F): ')).strip()
    if g == 'M':
        lmn.append(n)
        lmi.append(i)
    elif g == 'F':
        lfn.append(n)
        lfi.append(i)
    elif g != 'M' and g != 'F':
        print('Codigo incorreto para o sexo. Tente novamente.')
print('=' * 12)
print('A média de idade do grupo é {}' .format((sum(lmi) + sum(lfi)) / (len(lmi) + len(lfi)))
if len(lmi) != 0:
    x = lmi.index(max(lmi))  # Indice da lista de homens com a maior idade.
    print('O homem mais velho é {}.' .format(lmn[x].title()))
elif len(lfi) != 0:
    q = [z for z in lfi if z < 20] #lista de idade de mulheres com menos de 20 anos
    print('{} mulheres têm menos de 20 anos.' .format(len(q)))
