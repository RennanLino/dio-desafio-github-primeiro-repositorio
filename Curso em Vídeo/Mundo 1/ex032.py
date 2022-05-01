a = int(input('Digite o ano para saber se ele é bissexto: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto'. format(a))
else:
    print('O ano de {} não é bissexto'.format(a))
