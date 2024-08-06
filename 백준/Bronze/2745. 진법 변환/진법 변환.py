N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)

86846823611197163108337531226495015298096208677436155