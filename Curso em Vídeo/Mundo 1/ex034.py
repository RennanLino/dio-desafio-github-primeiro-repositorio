s = float(input('Salario: R$ '))
if s > 1250:
    print('O salário com aumento de 10% será {}' .format(s * 1.1))
else:
    print('O salário com 15% de aumento será {}' .format(s * 1.15))
