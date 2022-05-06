numero = int(input())

if (numero - 1) % 2 != 0:
    anterior = numero - 1
else:
    anterior = numero - 2

if (numero + 1) % 2 == 0:
    posterior = numero + 1
else:
    posterior = numero + 2

print(anterior, posterior)
