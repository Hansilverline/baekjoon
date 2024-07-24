import sys

n,m = map(int,sys.stdin.readline().split())

mat_1 = []
mat_2 = []

for i in range(n) :
    mat_1.append(list(map(int,input().split())))
for i in range(n) :
    mat_2.append(list(map(int,input().split())))

mat_3 = [[0 for i in range(len(mat_1[0]))] for j in range(len(mat_1))]

for i in range(n) :
    for j in range(m):
        mat_3[i][j] = mat_1[i][j] + mat_2[i][j]

for i in range(n) :
    for j in range(m):
        print(mat_3[i][j],end=' ')
    print()