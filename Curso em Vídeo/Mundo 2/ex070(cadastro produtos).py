#Lê nome e preco de produtos. pergunta se o usuario deseja continuar.
#mostra qual o total gasto na compra (s). quantos produtos custam mais de R$1000 (k). qual o nome do produto mais barato (bn).
s = k = bp = c = 0
bn = ''
while True:
    n = str(input('Produto: ')).strip().upper()
    p = float(input('Preço: R$ '))
    s += p
    c += 1
    if c == 1 or p < bp:
        bn = n
        bp = p
    if p > 1000:
        k += 1
    x = str(input('Quer registrar mais algum produto [S/N]? ')).strip().upper()
    while x not in 'SN':
        print('Código inválido.')
        x = str(input('Quer registrar mais algum produto [S/N]? ')).strip().upper()
    if x == 'N':
        break
print(f'O total gasto na compra foi {s}.'
      f'\n{k} produtos custaram mais de R$1000.'
      f'\nO produto mais barato foi {bn.title()}.')