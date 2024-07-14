n, m = map(int,input().split())
baguni = []
for a in range(n):
    baguni.append(0)
for b in range(m) :
    i,j,k = map(int,input().split())
    for i in range(i-1,j):
        baguni[i] = k
for i in range(len(baguni)):
    print(baguni[i],end=' ')