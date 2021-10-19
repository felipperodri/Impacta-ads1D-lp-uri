dia_da_compra = input()
prazo = int(input())
dias_da_semana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado','domingo','segunda','terca','quarta','quinta','sexta']
index_lista = dias_da_semana.index(dia_da_compra)
dia_da_entrega = dias_da_semana[index_lista+prazo]

if prazo == 0:
    print ('chega hoje!')
else:
    print (f'sera entregue {dia_da_entrega}')