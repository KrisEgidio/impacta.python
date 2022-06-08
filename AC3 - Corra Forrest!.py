def addTempo(n):
    tempos.append(n)

def calcularMedia():
    return sum(tempos) / float(len(tempos))


tempo = int(input())
tempos = []

while tempo >= 0:
    addTempo(tempo)
    tempo = int(input())


media = calcularMedia()
print(f'MEDIA: {media:.2f}')

for i in tempos:
    if i < media:
        print(i)
