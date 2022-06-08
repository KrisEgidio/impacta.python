def exibirTabuada(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

def linha():
    print('-'*10)


primeiro = int(input())
segundo = int(input())

ehMenor = primeiro < segundo
ehIgual = primeiro == segundo

if ehMenor:
    for x in range(primeiro, segundo + 1): 
        exibirTabuada(x)
        linha()
elif ehIgual:
    exibirTabuada(primeiro)
    linha()
else:
    print('Nenhuma tabuada no intervalo!')
