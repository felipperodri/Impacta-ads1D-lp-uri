A = int(input())
B = int(input())

if A > B:
    print('Nenhuma tabuada no intervalo!')
else:
    for num in range(A, B + 1):
        for i in range(1, 10 + 1):
            print(f'{num} x {i} = {num * i}')
        print('----------')