dia_compra = input()
qtd_dias = int(input())
if qtd_dias < 0 or qtd_dias > 6:
        print('Insira um prazo válido')
elif qtd_dias == 0:
        print('chega hoje!')
else:

    if dia_compra == 'domingo':
        if qtd_dias == 1:
            print('sera entregue segunda')
        elif qtd_dias == 2:
            print('sera entregue terca')
        elif qtd_dias == 3:
            print('sera entregue quarta')
        elif qtd_dias == 4:
            print('sera entregue quinta')
        elif qtd_dias == 5:
            print('sera entregue sexta')
        elif qtd_dias == 6:
            print('sera entregue sabado')
    elif dia_compra == 'segunda':
        if qtd_dias == 1:
            print('sera entregue terca')
        elif qtd_dias == 2:
            print('sera entregue quarta')
        elif qtd_dias == 3:
            print('sera entregue quinta')
        elif qtd_dias == 4:
            print('sera entregue sexta')
        elif qtd_dias == 5:
            print('sera entregue sabado')
        elif qtd_dias == 6:
            print('sera entregue domingo')
    elif dia_compra == 'terca':
        if qtd_dias == 1:
            print('sera entregue quarta')
        elif qtd_dias == 2:
            print('sera entregue quinta')
        elif qtd_dias == 3:
            print('sera entregue sexta')
        elif qtd_dias == 4:
            print('sera entregue sabado')
        elif qtd_dias == 5:
            print('sera entregue domingo')
        elif qtd_dias == 6:
            print('sera entregue segunda')
    elif dia_compra == 'quarta':
        if qtd_dias == 1:
            print('sera entregue quinta')
        elif qtd_dias == 2:
            print('sera entregue sexta')
        elif qtd_dias == 3:
            print('sera entregue sabado')
        elif qtd_dias == 4:
            print('sera entregue domingo')
        elif qtd_dias == 5:
            print('sera entregue segunda')
        elif qtd_dias == 6:
            print('sera entregue terca')
    elif dia_compra == 'quinta':
        if qtd_dias == 1:
            print('sera entregue sexta')
        elif qtd_dias == 2:
            print('sera entregue sabado')
        elif qtd_dias == 3:
            print('sera entregue domingo')
        elif qtd_dias == 4:
            print('sera entregue segunda')
        elif qtd_dias == 5:
            print('sera entregue terca')
        elif qtd_dias == 6:
            print('sera entregue quarta')
    elif dia_compra == 'sexta':
        if qtd_dias == 1:
            print('sera entregue sabado')
        elif qtd_dias == 2:
            print('sera entregue domingo')
        elif qtd_dias == 3:
            print('sera entregue segunda')
        elif qtd_dias == 4:
            print('sera entregue terca')
        elif qtd_dias == 5:
            print('sera entregue quarta')
        elif qtd_dias == 6:
            print('sera entregue quinta')
    elif dia_compra == 'sabado':
        if qtd_dias == 1:
            print('sera entregue domingo')
        elif qtd_dias == 2:
            print('sera entregue segunda')
        elif qtd_dias == 3:
            print('sera entregue terca')
        elif qtd_dias == 4:
            print('sera entregue quarta')
        elif qtd_dias == 5:
            print('sera entregue quinta')
        elif qtd_dias == 6:
            print('sera entregue sexta')