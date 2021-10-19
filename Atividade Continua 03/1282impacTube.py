n = int(input())
temp = []
tabela = []

for canais in range(1, n + 1):
    nome, inscritos, monet, premium = input().split(";")
    inscritos = int(inscritos)
    monet = float(monet)
    temp.extend([nome, inscritos, monet, premium])
    temp.append(0)
    tabela.append(temp)
    temp = []

fixo1 = float(input())
fixo2 = float(input())

print(f'-----')
print(f'BÔNUS')
print(f'-----')

qtd_bonus = 0

for cont in range(len(tabela)):
    qtd_bonus = 0
    aux = tabela[cont][1]
    while aux >= 1000:
        aux -= 1000
        qtd_bonus += 1
    tabela[cont][4] = qtd_bonus



for i in range(len(tabela)):
    if 'sim' in tabela[i]:
        bonus = tabela[i][2] + (tabela[i][4] * fixo1)
        print(f'{tabela[i][0]}: R$ {bonus:.2f}')
    else:
        bonus = tabela[i][2] + (tabela[i][4] * fixo2)
        print(f'{tabela[i][0]}: R$ {bonus:.2f}')