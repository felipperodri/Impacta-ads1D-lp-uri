idade = int(input())
contador = 1
soma = 0
soma += idade

while idade > 0:
    idade = int(input())
    if idade <= 0: break
    contador += 1
    soma += idade
    

resultado = soma / contador
print(f'{resultado:.2f}')