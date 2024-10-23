def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def combination(a,b):
    return factorial(a) // (factorial(b) * factorial(a - b))

t = int(input())

for i in range(t) :
    n,m = map(int,input().split())
    if n == m :
        result = 1
    elif n > m :
        result = combination(n,m)
    else :
        result = combination(m,n)
    print(result)
