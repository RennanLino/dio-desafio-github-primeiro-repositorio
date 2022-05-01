a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
from random import choice
e = choice([a, b, c, d])
print('O aluno escolhido foi {}' .format(e))
