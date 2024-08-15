n_count = int(input())
n_divisor = list(map(int,input().split()))
n = 0
n_divisor.sort()
if len(n_divisor) % 2 == 0 :
    n = n_divisor[0]*n_divisor[-1]
else :
    n = n_divisor[int(len(n_divisor)/2)]**2

print(n)