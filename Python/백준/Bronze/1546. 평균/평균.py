n = int(input())
scores = []
for i in range(n):
    scores.append(0)
scores = list(map(int,input().split()))
m = max(scores)
sum = 0
for i in scores :
    i = i/m*100
    sum += i
print(sum/n)