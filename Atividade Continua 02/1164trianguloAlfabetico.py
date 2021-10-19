letras = ['A','B','C','D','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T','U','V',
'W','X','Y','Z']
while True:
    num = int(input())
    if 1 <= num and num <= 26: break

for x in range(1, num + 1):
    letra = letras[x-1]
    print(letra * (x))