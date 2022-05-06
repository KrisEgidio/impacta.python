#Crie um programa para um site! O programa deverá solicitar o valor de um item
# e a qtd de unidades compradas deste item, ao final deve exibir o total com
#desconto de 10%. Considere que a qtd será um número natural positivo

valor = float(input("Digite o valor do item: "))
qtd = int(input("Digite a quantidade desejada: "))

desconto = (valor * qtd) * 0.1
valorFinal = (valor * qtd) - desconto

print(f"O total a pagar é de R$ {valorFinal:.2f}")
