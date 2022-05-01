# Programa para calcular parcelas de empréstimo bancário na compra de uma casa
v = float(input('Valor da casa: '))
s = float(input('Salário do comprador: R$ '))
t = int(input('Tempo para pagamento em anos: '))
p = v / (t * 12)
if p > 0.3 * s:
    print('O valor da prestação excede 30% do salário do comprador.\n'
          'O emprestimo foi negado')
else:
    print('O valor da prestação será de R$ {:.2f}' .format(p))