n = int(input())

for i in range(n,3,-1) :
    numbers = list(str(i))
    cnt = 0
    for number in numbers :
        if number in ['4','7'] :
            cnt += 1
    if cnt == len(numbers) :
        print(i)
        break