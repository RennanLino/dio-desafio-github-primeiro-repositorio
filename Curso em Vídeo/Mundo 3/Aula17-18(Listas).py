#Aula 17
print('-='*40)
a = [2, 3, 4, 7]
b = a #Cria ligação com a lista 'a'
c = a[:] #Cria cópia da lista 'a'
print(f'Lista A: {a}')
print(f'Lista B: {b}')
for x, y in enumerate(a):
    print(f'Na posição {x} encontrei o valor {y}!')
print('Cheguei ao final da lista.')
# Aula 18
print('-='*40)
dados = ['Pedro, 25']
pessoas = list()
pessoas.append(dados[:]) #a lista dados, é o primeiro elemento da lista pessoas
print(pessoas)
pessoas = [['Pedro, 25'], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1])
#pratica
print('-='*40)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
for p in pessoas:
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')
#pratica
print('-='*40)
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menos de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')