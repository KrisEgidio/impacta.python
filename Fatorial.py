numero = int(input())
fatorial = 1
i = 1

for x in range(numero + 1):
    if fatorial < 13:
        fatorial *=  (numero - i)
        i += 1
        print(fatorial)


print(fatorial * 1)

