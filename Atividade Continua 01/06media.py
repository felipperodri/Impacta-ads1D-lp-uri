trab = float(input())
prova_reg = float(input())
media_final = (trab + prova_reg) / 2

if media_final >= 6:
    print('aprovado')
elif trab >= 2:
    print('talvez com a sub')
else:
    print('reprovado')
