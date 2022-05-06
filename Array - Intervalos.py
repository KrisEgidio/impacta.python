informado = float(input())
intervalos = [[0,25], [25,50], [50,75], [75,100]]
intervaloFoiInformado = False

for intervalo in intervalos:
    inicio = float(intervalo[0])
    fim = float(intervalo[1])
    if informado > inicio and informado <= fim:
        print("Intervalo ", intervalo)
        intervaloFoiInformado = True

if intervaloFoiInformado == False:
    print("Fora de intervalo")
