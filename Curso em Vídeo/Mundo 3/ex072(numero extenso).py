n = int(input('Digite um número entre 0 e 20: '))
e = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
     'dezesete', 'dezoito', 'dezenove', 'vinte')
while n < 0 or 20 < n:
    print('Tente novamente.')
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {e[n]}')
