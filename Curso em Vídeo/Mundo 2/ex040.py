#Calcula a média entre duas notas, e avisa sobre aprovação
cor = {'vermelho':'\033[1;31m',
       'verde':'\033[1;32m',
       'limpa':'\033[m',}
a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
m = (a + b) / 2
if m < 5:
    print('Média do Aluno: {}\n'
          'Situação: {}REPROVADO{}' .format(m, cor['vermelho'], cor['limpa']))
elif 5 <= m <= 6.9:
    print('Média do Aluno: {}\n'
          'Situação: RECUPERAÇÃO' .format(m)
else:
    print('Média do Aluno: {}\n'
          'Situação: {}APROVADO{}' .format(m, cor['verde'], cor['limpa']))
