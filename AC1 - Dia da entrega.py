dia = input()
qtdDias = int(input())
dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta','sabado']
index = dias.index(dia)

if qtdDias > 0:
    for x in range(0,qtdDias):
        if index < 6:
            index += 1
        else:
            index = 0

    print('sera entregue',dias[index])
else:
    print('chega hoje!')


