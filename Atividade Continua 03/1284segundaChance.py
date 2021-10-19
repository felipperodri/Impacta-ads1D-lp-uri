notas = []
notas_atv = []
novas_notas = []
notas_alteradas = 0
cont = 1
n = int(input())

for alunos in range(1, n + 1):
    nota = float(input())
    notas.append(nota)
for alunos in range(1, n + 1):
    nota_atv = float(input())
    notas_atv.append(nota_atv)

for i in range(len(notas_atv)):
    if notas_atv[i] == 10 and notas[i] < 10:
        notas_alteradas += 1
        novas_notas.append(notas[i] + 2)
    else:
        novas_notas.append(notas[i])
print(f'NOTAS ALTERADAS: {notas_alteradas}')

novas_notas = [10 if x >10 else x for x in novas_notas]


for x in range(len(novas_notas)):
    if novas_notas[x] != notas[x]:
        print(f'*(00{cont}) original: {notas[x]:05.2f} | final: {novas_notas[x]:05.2f}')
    else:
        print(f'-(00{cont}) original: {notas[x]:05.2f} | final: {notas[x]:05.2f}')
    cont += 1
