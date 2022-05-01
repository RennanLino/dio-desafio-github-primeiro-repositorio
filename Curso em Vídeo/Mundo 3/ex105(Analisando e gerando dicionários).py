def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    l = [*num]
    d = {'Total': len(l), 'Maior': max(l), 'Menor': min(l), 'Média': sum(l)/len(l)}
    if sit == True:
        if d['Média'] < 5:
            d['Situação'] = 'RUIM'
        elif 5 <= d['Média'] < 7:
            d['Situação'] = 'RAZOÁVEL'
        elif 7 <= d['Média']:
            d['Situação'] = 'BOA'
    return d


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)