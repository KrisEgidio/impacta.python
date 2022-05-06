preco = float(input())
qtd = int(input())

valor = preco * qtd
desconto = (valor * 0.1) + ((valor * qtd) / 100)
total = valor - desconto

print(f'{valor:.2f}')
print(f'{total:.2f}')
