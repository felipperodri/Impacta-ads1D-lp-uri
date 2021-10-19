casosTeste = int(input())
for x in range(casosTeste):
    pontosJoao = 0
    pontosMaria = 0

    for joao in range(3):
        pontuacao, distancia = map(int, input().split())
        pontosJoao += pontuacao * distancia

    for maria in range(3):
        pontuacao, distancia = map(int, input().split())
        pontosMaria += pontuacao * distancia

    if pontosJoao > pontosMaria:
        print('JOAO')
    else:
        print('MARIA')