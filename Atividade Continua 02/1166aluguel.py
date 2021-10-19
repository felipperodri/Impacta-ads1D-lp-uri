divida = int(input())
pagamento = int(input())
contador = 1

while divida > pagamento:
    print(f'pagamento: {contador}')
    print(f'antes = {divida}')
    print(f'depois = {divida - pagamento}')
    print('-----')
    divida = divida - pagamento
    contador += 1
if divida <= pagamento:
    print(f'pagamento: {contador}')
    print(f'antes = {divida}')
    print(f'depois = 0')
    print('-----')