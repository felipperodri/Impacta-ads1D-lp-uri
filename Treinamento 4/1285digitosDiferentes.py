while True:
    try:
        N, M = map(int, input().split())
        qtd = 0

        for x in range(N, M + 1):
            if len(set(list(str(x)))) == len(str(x)):
                qtd += 1
        print(qtd)
    except EOFError:
        break
