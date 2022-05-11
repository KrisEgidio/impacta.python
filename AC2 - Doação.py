doacao = 0
valor = 0

while valor >= 0:
    doacao += valor
    valor = float(input())

total = doacao * 2.50
print(f'VC$ {doacao:.2f}')
print(f'R$ {total:.2f}')
   
