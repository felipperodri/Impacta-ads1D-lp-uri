inicio = int(input())
fim = int(input())
contador = 0

for x in range(inicio, fim + 1):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        print(f'{x}')
        contador += 1
print(f'bissextos: {contador}')
