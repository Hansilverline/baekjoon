while(1) :

    n = int(input())
    
    if n == -1 :
        break

    yaksu = []
    isPerfect = 0

    for i in range(1,int((n/2)+1)):
        if n % i == 0 :
            yaksu.append(i)
            # 약수를 저장해둔 리스트
    for i in yaksu :
        isPerfect += i 
    
    if isPerfect == n :
        print(n,'=',yaksu[0],end=' ')
        for i in range(1,len(yaksu)) :
            print('+',yaksu[i],end=' ')
        print()
    else :
        print(n,'is NOT perfect.')