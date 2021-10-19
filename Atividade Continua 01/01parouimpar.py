x = int(input())
if x < 2:
    print('Digite um valor maior ou igual a 2.')
elif x % 2 == 0:
    print(f'{x - 1} {x + 2}')
elif x % 2 != 0:
    print(f'{x - 2} {x + 1}')