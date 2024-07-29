square = [[0 for i in range(101)] for j in range(101)]

n = int(input())

for i in range(n) :
    x,y = map(int,input().split())

    for row in range(x,x+10) :
        for col in range(y,y+10) : 
            square[row][col] = 1

cnt = 0
for i in square : 
    cnt += i.count(1)
print(cnt)