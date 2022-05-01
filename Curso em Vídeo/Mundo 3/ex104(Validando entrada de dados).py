def leiaInt(a):
    while True:
        x = input(f'{a}')
        if x.isnumeric():
            x = int(x)
            return x
            break
        else:
            print(f'\033[;31mErro! Digite um número inteiro válido.\033[m')


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')