x,y = input().split()

def Rev(a) :
    a = list(a)
    reversed_list = [] 
    for i in a[::-1]:
        reversed_list.append(i)
    result = ''.join(map(str, reversed_list))
    return result

lastPara = int(Rev(x))+int(Rev(y))
result = Rev(str(lastPara))
print(int(result))