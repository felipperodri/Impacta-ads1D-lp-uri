def adicionar(v, item=True):
    v.append(item)
    v.sort()
    return

def remover (v, item=True):
    if item in v:
        v.remove(item)
    else:
        print(f'código {item} não encontrado')
    return



carrinho = list(map(int, input().split()))
carrinho.sort()


comandos = input().split()
if len(comandos) == 2:
    comando, item = comandos
    item = int(item)
else:
    comando = comandos[0]
    item = 'padrao'

while comandos[0] != 'encerrar':
    if comandos[0] == 'adicionar':
        adicionar(carrinho,item)
    elif comandos[0] == 'remover':
        remover(carrinho, item)
    elif comandos[0] == 'exibir':
        print(*carrinho, sep = " ")
    
    comandos = input().split()
    if len(comandos) == 2:
        comando, item = comandos
        item = int(item)
    else:
        comando = comandos[0]
        item = 'padrao'
print(*carrinho, sep = " ")