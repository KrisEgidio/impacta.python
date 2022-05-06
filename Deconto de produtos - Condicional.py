# Crie um programa que receba como entrada o valor de um produto 
# e a quantidade comprada. O programa concederá 10% de desconto 
# para compras com total maior ou igual à R$ 100,00.

valor = float(input("Digite o valor do produto: "))
qtd = int(input("Digite a quantidade: "))

total = valor * qtd;

if total >= 100:
    total -= total * 0.1

print(f"O valor total é R${total:.2f}") 
