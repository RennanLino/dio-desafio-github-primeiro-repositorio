#Tuplas são imutaveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(sorted(lanche))
'''for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5, 1))
print(lanche.index('Hamburguer'))