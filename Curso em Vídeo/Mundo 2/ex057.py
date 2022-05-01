#Pergunta o sexo da pessoa, caso digitem errado pergunta novamente
s = str(input('Sexo [M/F]: ')).upper().strip()
while s != 'M' and s != 'F':
    print('Código inválido. Tente novamente.')
    s = str(input('Sexo [M/F]: ')).upper().strip()
print('Acabou.')