#Informa o preço de um  produto a partir da forma de pagamento
p = float(input('Preço do produto: R$ '))
print('Digite o número correspondente à forma de pagamento.\n'
      '1 - À vista\n'
      '2 - À vista no cartão\n'
      '3 - Em 2x no cartão\n'
      '4 - Em 3x ou mais no cartão')
f = int(input('Forma de pagamento: '))
if f ==1:
      np = p * 0.9
      print('À vista o preço será de R$ {:.2f}' .format(np))
elif f == 2:
      np = p * 0.95
      print('À vista no cartão o preço será de R$ {:.2f}' .format(np))
elif f == 3:
      np = p
      print('Em 2x no cartão o preço será de R$ {:.2f}, com parcelas de R$ {}'.format(np, np / 2))
elif f == 4:
      np = p * 1.2
      x = int(input('Em quantas vezes será dividido: '))
      print('Em {}x no cartão o preço será de R$ {:.2f}, com parcelas de {}'.format(x, np, np / x))
else:
      print('Bruh')