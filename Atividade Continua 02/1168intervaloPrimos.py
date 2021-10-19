inicio = int(input())
fim = int(input())
primos = 0

for numero in range(inicio, fim + 1):
    if numero > 1:
        for x in range(2, numero):
            if numero % x == 0:
                break
        else:
            print(numero)
            primos += 1
print(f'primos: {primos}')