def alfabeto():
    """Retorna array com alfabeto em maiusculo"""
    return [chr(i) for i in range(ord('A'),ord('Z') + 1)]

numero = int(input())
alfabeto = alfabeto()
contador = 0

for i in range(numero):
    print(alfabeto[contador] * (i + 1))
    contador += 1
    
