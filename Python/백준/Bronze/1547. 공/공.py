times = int(input())
numbering = 1

for i in range(times):
    x,y = map(int,input().split())
    if (x == numbering or y == numbering) :
        if x == numbering :
            numbering = y
        else :
            numbering = x

print(numbering)
