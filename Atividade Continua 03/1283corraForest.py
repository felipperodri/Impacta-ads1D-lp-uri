qtd_tempos = 0
soma_tempos = 0
tempos = []

while True:
    tempo = int(input())
    if tempo < 0:
        break
    tempos.append(tempo)
    qtd_tempos += 1
    soma_tempos += tempo
media_tempos = soma_tempos / qtd_tempos
print(f'MEDIA: {media_tempos:.2f}')
for x in tempos:
    if x < media_tempos:
        print(x)