#Calcula IMC e informa grau de obesidade
p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
imc = p / a ** 2
if imc < 18.2:
    print('A pessoa está abaixo do peso ideal')
elif 18.2 <= imc <= 25:
    print('A pessoa se encontra no peso ideal.')
elif 25 < imc <= 30:
    print('A pessoa está com sobrepeso.')
elif 30 < imc <= 40:
    print('A pessoa está obesa.')
else:
    print('A pessoa se encontra em obesidade mórbida.')
