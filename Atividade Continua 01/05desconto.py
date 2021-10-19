preco = float(input())
qtd = int(input())
preco_total = preco * qtd
desc = preco_total * (0.1 + qtd * 0.01)
print(f'{preco_total:.2f}')
print(f'{preco_total - desc:.2f}')