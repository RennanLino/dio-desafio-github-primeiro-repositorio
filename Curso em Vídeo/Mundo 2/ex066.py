#Ex064 utilizando o break
s = c = 0
while True:
    n = float(input('Digite um número [999 p/ parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} números foram digitados, e a média entre ele foi {s / c}')