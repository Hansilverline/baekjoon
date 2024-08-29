numbers = list(map(int,input().split()))

# [0,4,2,5,6]
sum = 0

for i in range(len(numbers)) :
    sum += (numbers[i]**2)
    last = sum % 10

print(last)