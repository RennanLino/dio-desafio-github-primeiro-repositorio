# Cadastra número indefinido de pessoas. Informa quantas tem mais de 18 anos, quantos homens e quantas mulheres com
#menos de 20 anos foram cadastradas
p18 = 0
h = 0
m20 = 0
while True:
    i = int(input('Idade: '))
    if i > 18:
        p18 += 1
    s = str(input('Sexo [M/F]: ')).strip().upper()
    while s not in 'MF':
        print('Opção inválida para sexo.')
        s = str(input('Sexo [M/F]: ')).strip().upper()
    if s == 'M':
        h +=1
    elif s == 'F' and i < 20:
        m20 +=1
    x = str(input('Deseja continuar [S/N]?')).strip().upper()
    if x == 'N':
        break
    while x != 'N' and x != 'S':
        print('Opção inválida.')
        x = str(input('Deseja continuar [S/N]?')).strip().upper()
print(f'{p18} pessoas acima de 18 anos foram cadastradas.'
      f'\n{h} homens foram cadastrados.'
      f'\n{m20} mulheres abaixo de 20 anos foram cadastradas.')