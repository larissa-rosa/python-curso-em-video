def notas(* n, situação=False):
    """
    Função para analisar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opcional, indicando se deve ou não informar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if situação:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r


resp = notas(5.5, 2.5, 9, 8.5, situação=True)
print(resp)
