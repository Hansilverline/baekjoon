num = list(map(int,input().split()))

for i in range(min(num),1000001) :
    cnt=0
    for n in num : 
        if i % n == 0 :
            cnt += 1

    if cnt > 2 : 
        print(i)
        break