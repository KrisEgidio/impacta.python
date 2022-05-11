divida = int(input())
mensalidade = int(input())
pagamento = 1

while divida > 0:
    print('pagamento:',pagamento)
    print('antes =', divida)
    if((divida - mensalidade) > 0):
        print('depois =', divida - mensalidade)
    else:
        print('depois = 0')
    print('-----')
    print()
    divida -= mensalidade
    pagamento += 1
    
