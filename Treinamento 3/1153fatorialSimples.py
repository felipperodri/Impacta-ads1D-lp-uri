N = int(input())
resultado = 1
contador = 1

while True:
    if 0 < N < 13: break

while contador <= N:
    resultado = resultado * contador
    contador += 1
print(resultado)