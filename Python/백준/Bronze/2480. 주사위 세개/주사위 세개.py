A,B,C = map(int,input().split())
coin = 0
if A == B == C :
    coin = 10000+(A*1000)
elif A == B or A == C :
    coin = 1000+A*100
elif B == C :
    coin = 1000+B*100
else : 
    coin = max(A,B,C)*100
print(coin)