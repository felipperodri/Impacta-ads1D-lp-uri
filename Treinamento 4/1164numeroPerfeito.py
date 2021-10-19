casosTeste = int(input())


for i in range(casosTeste):
    numero = int(input())
    soma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor
    if soma == numero:
        print(f'{numero} eh perfeito')
    else:
        print(f'{numero} nao eh perfeito')