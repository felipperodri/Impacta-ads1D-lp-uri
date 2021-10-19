casosTeste = int(input())
responsaveis = [' ','Rolien','Naej','Elehcim', 'Odranoel']

for i in range(casosTeste):
    feedbacks = int(input())
    for j in range(feedbacks):
        categoria = int(input())
        print(responsaveis[categoria])
