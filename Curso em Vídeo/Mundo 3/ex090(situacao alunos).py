d = {}
d['nome'] = str(input('Nome: '))
d['media'] = float(input(f'Média de {d["nome"]}: '))
print(f'O nome do aluno é: {d["nome"]}')
print(f'A média de {d["nome"]} é igual a {d["media"]}')
if d['media'] >= 7:
    print('Situação do aluno: Aprovado')
else:
    print('Situação do aluno: Reprovado')
