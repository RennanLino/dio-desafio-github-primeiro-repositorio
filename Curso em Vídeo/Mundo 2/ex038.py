# Programa para comparar dois números inteiros, mostrando o maior
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O primeiro valor é maior')
elif a < b:
    print('O segundo valor é maior')
else:
    print('Os dois valores digitados são iguais')