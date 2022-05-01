#Joga par ou ímpar. O jogo só é interrompido quando o jogador perde.
from random import randint
print('=-' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 13)
t = 0
while True:
    c = randint(0, 10)
    n = int(input('Diga um valor: '))
    u = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    while u != 'P' and u != 'I':
        print('Jogada inválida. Tente novamente')
        u = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    s = c + n
    print('-' * 57)
    if s % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s}, deu PAR')
        print('-' * 57)
    elif s % 2 != 0:
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s}, deu ÍMPAR.')
        print('-' * 57)
    if s % 2 == 0 and u == 'P' or s % 2 != 0 and u  == 'I':
        t += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 13)
    elif s % 2 == 0 and u == 'I' or s % 2 != 0 and u  == 'P':
        print('Você PERDEU!')
        break
print(f'GAME OVER! você venceu {t} vezes.')