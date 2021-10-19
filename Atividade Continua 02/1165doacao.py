doacao = float(input())
soma = 0

while doacao != -1.0:
    soma = soma + doacao
    doacao = float(input())
print(f'VC$ {soma:.2f}')
print(f'R$ {soma * 2.5:.2f}')