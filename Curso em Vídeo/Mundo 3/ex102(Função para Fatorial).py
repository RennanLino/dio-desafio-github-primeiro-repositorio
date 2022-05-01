def fatorial(a, show=False):
    f = 1
    for b in range(a, 0, -1):
        if show == True:
            if b > 1:
                print(f'{b} x ', end='')
            else:
                print('= ', end='')
        f *= b
    return f


#Programa principal
print(fatorial(5))