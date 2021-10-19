n = int(input())
numeros = 1
qtd_pares = 0

while numeros <= 5:
    if n % 2 == 0:
        qtd_pares += 1
    if numeros == 5: break
    n = int(input())
    numeros += 1
print(f'{qtd_pares} valores pares')
