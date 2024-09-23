yundooName = input().upper()
num = int(input())
hubo = []
percentList = []

for _ in range(num):
    hubo.append(input().upper())
hubo.sort(reverse=False)

for i in range(num) :
    fullName = hubo[i]+yundooName
    L = fullName.count('L')
    O = fullName.count('O')
    V = fullName.count('V')
    E = fullName.count('E')
    percent = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    percentList.append(percent)

print(hubo[percentList.index(max(percentList))])