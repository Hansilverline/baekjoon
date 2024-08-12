T = int(input())

rest_list =[]

for i in range(T) :
    rest_list =[]
    n = int(input())
    rest_list.append(n//25)
    n = n%25
    rest_list.append(n//10)
    n = n%10
    rest_list.append(n//5)
    n = n%5
    rest_list.append(n//1)
    print(*rest_list)
