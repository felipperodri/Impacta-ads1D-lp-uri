cont_epr = 0
cont_ehd = 0
intrusos = 0

while True:
    try:
        n = int(input())
        for alunos in range(1, n + 1):
            matricula, curso = input().split(" ")
            for _ in range(1, alunos + 1):
                if curso == "EPR":
                    cont_epr += 1
                    break
                elif curso == "EHD":
                    cont_ehd += 1
                    break
                else:
                    intrusos += 1
                    break
        print(f'EPR: {cont_epr}')
        print(f'EHD: {cont_ehd}')
        print(f'INTRUSOS: {intrusos}')
        cont_epr = 0
        cont_ehd = 0
        intrusos = 0   
    except EOFError:
        break