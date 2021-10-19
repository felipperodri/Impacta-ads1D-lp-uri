X = int(input())
Y = int(input())
soma = 0

for numero in range(Y + 1, X):
    if numero % 2 == 0:
        continue
    else:
        soma += numero
print(soma)