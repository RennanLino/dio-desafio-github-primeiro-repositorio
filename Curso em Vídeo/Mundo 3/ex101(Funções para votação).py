from datetime import datetime


def voto(ano):
    if datetime.now().year - ano <= 16:
        print('Você ainda não tem direito ao voto.')
    elif 16 < datetime.now().year - ano < 18 or datetime.now().year - ano >= 70:
        print('Você tem direito ao voto facultativo.')
    elif 18 <= datetime.now().year - ano < 70:
        print('Você tem a obrigatoriedade de votar.')


#Programa Principal
ano = int(input('Digite o seu ano de nascimento: '))
voto(ano)