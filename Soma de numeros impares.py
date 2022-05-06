n = int(input())
start = 2
end = n + 1

for x in range(start, end):
    if x % 2 == 0:
        print(start,"^2 = ", x**2, sep = '')
        start += 2
