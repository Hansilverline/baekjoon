n =int(input())
m =int(input())

sosu = []
for number in range(n,m+1) :
    # 60,61,62,63,,,,,,
    yaksu = []
    for i in range(1,int(number/2)+1):
        # 1,2,3,4,,,30
        if number % i == 0 :
            yaksu.append(i)
    if len(yaksu) == 1 : 
        sosu.append(number)

if len(sosu) == 0 :
    print(-1)
else: 
    print(sum(sosu))
    print(min(sosu))