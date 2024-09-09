import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

total = 0
X = m

if m + T > M :
    print(-1)
else : 
    while N>0 :
        if X+T <= M :
            X = X+T
            N-=1
        else :
            X = max(X-R,m)
        total+=1

    print(total)
