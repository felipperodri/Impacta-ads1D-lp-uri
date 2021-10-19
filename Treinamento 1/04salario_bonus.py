nome = input()
sal_fixo = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
sal_final = sal_fixo + comissao

print(f'TOTAL = R$ {sal_final:.2f}')