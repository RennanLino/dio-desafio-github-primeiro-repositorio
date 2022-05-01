from datetime import datetime
d = {}
d['nome'] = str(input('Nome: '))
d['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
d['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['ctps'] != 0:
    d['contratação'] = int(input('Ano de Contratação: '))
    d['salario'] = int(input('Salário: R$ '))
    d['aposentadoria'] = d['contratação'] + 35 - datetime.now().year
print('-='*20)
for k, v in d.items():
    print(f'  — {k} tem o valor {v}')