casos = int(input())
divisores = 0

for _ in range(1, casos + 1):
    divisores = 0
    numero = int(input())
    for x in range(1, numero + 1):
        if numero % x == 0:
             divisores += 1
    if divisores == 2:
        print(f'{numero} eh primo')
    else:
        print(f'{numero} nao eh primo')