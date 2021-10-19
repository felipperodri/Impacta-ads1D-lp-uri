N = int(input())

while True:
    if 5 < N < 2000:
        break
for numero in range(1, N + 1):
    if numero % 2 != 0:
        continue
    else:
        resultado = numero ** 2
        print(f'{numero}^2 = {resultado}')