def adicionar(n):
    carrinho.append(n)

def exibir():
    carrinho.sort()
    for i in range(0, len(carrinho)-1):
        print(carrinho[i], end=' ')
    print(carrinho[len(carrinho)-1])

def remover(n):
    elemento_existe = n in carrinho
    if elemento_existe:
        carrinho.remove(n)
    else:
        print(f'código {n} não encontrado')

itens = input().split()
if len(itens) > 0:
    carrinho = [int(i) for i in itens]
else:
    carrinho = []

finalizar_compra = False

while finalizar_compra == False:
    informacao = input().split()
    acao = informacao[0]
    if acao == 'exibir':
        exibir()
    elif acao == 'adicionar':
        item = int(informacao[1])
        adicionar(item)
    elif acao == 'remover':
        item = int(informacao[1])
        remover(item)
    else:
        finalizar_compra = True
        if len(carrinho) > 0:
            exibir()
        

