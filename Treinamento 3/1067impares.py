X = int(input())

while True:
    if 1 <= X <= 1000: break

for numero in range(1, X + 1):
    if numero % 2 == 0:
        continue
    else:
        print(numero)  