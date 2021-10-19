numero = int(input())
maior_numero = numero
maior_pos = 1
qtd_numeros = 1

while qtd_numeros < 5:
    n = int(input())
    qtd_numeros += 1
    if n > maior_numero:
        maior_numero = n
        maior_pos = qtd_numeros
    
print(maior_numero)
print(maior_pos)
