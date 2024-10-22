n = int(input())
numbers = list(map(int,input().split()))
cnt = 0

client = [0 for _ in range(101)]

for number in numbers :
    if client[number] == 0 :
        client[number] = 1
    else :
        cnt += 1

print(cnt)