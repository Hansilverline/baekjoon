n,m = map(int,input().split())
baguni = []
temp = []
for i in range(n) :
    baguni.append(i+1)

for i in range(m):
    i,j = map(int,input().split())
    temp = baguni[i-1:j]
    temp.reverse()
    baguni[i-1:j] = temp

for i in baguni :
    print(i,end=' ')