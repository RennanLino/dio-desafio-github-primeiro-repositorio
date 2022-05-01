# Faz contagem regressiva, com pausa de 1 segundo
from time import sleep
for a in range(10, 0, -1):
    print(a)
    sleep(1)
print('HAPPY NEW YEAR!')