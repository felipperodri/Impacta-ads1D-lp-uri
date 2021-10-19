def tabuada(n):
    for x in range(1, 11):
        print(f'{n} x {x} = {n * x}')


while True:
    n = int(input())
    if 0 <= n <= 10: break
tabuada(n)
