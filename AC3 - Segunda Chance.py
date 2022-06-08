qtd_alunos = int(input())
notas_originais = []
notas_alteradas = []
notas_foram_alteradas = []
qtd_notas_alteradas = 0

for i in range(0, qtd_alunos):
    notas_originais.append(int(input()))

for i in range(0, qtd_alunos):
    notas_alteradas.append(int(input()))

for i in range(0, qtd_alunos):
    if notas_alteradas[i] == 10 and notas_originais[i] < 10:
        nova_nota = notas_originais[i] + 2
        notas_foram_alteradas.append(True)
        if nova_nota > 10.00:
            nova_nota = 10
        notas_alteradas[i] = nova_nota
    else:
        nova_nota = notas_originais[i]
        notas_alteradas[i] = nova_nota
        notas_foram_alteradas.append(False)


for i in range(0, qtd_alunos):
    if notas_foram_alteradas[i]:
        qtd_notas_alteradas += 1
        
print(f'NOTAS ALTERADAS: {qtd_notas_alteradas}')


for i in range(0, qtd_alunos):
    nota_original = notas_originais[i]
    nota_final = notas_alteradas[i]
    if notas_foram_alteradas[i]:
        caractere = '*'
    else:
        caractere = '-'
    aluno = i + 1
    print(f'{caractere}({aluno:0>3}) original: {nota_original:0>2}.00 | final: {nota_final:0>2}.00')
