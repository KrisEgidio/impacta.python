notaTrabalho = float(input())
notaProva = float(input())

media = (notaTrabalho + notaProva) / 2

if media < 6 and notaTrabalho < 2:
    print('reprovado')
elif media < 6:
    print('talvez com a sub')
else:
    print('aprovado')
