nome = input('Nome copmpleto: ').strip()
lista = nome.split()
print('Primeiro nome: {}' .format(lista[0]))
print('Ultimo nome: {}' .format(lista[len(lista) - 1]))
