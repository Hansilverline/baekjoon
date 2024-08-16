n = int(input())
num = n
count = 0

while(1) :
    c = (num//10) + (num%10)
    num = (num%10)*10 + (c%10)
    count += 1
    if num==n:
        break
print(count)