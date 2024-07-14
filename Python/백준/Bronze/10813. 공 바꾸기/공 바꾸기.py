n, m = map(int,input().split())
baguni = []
for a in range(1,n+1):
    baguni.append(a)
for b in range(m) :
    i,j = map(int,input().split())
    baguni[i-1],baguni[j-1] = baguni[j-1],baguni[i-1]
for i in range(len(baguni)):
    print(baguni[i],end=' ')