a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
lista = [a, b, c, d]
from random import shuffle
shuffle(lista)
print('A ordem de apresentação será: {}' .format(lista))