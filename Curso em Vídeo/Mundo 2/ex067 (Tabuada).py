#Mostra a tabuada de vários números para cada valor digitado pelo usuário. o programa é interrompido quando o valor digitado por negativo
while True:
    print('=' * 40)
    x = int(input('Digite um número p/ ver sua tabuada: '))
    print('=' * 40)
    if x < 0:
        break
    c = 1
    while c != 11:
        print(f'{x:2} x {c:2} = {x * c:2}')
        c += 1
