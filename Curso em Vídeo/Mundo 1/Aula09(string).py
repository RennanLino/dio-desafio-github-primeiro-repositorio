'''C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'''
frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[9:14])
print(frase[:2])
print(frase[9:])
print(frase[::2])
print('''Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), 
lower(), capitalize(), title(), strip(), junção com join().''')
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][1])
