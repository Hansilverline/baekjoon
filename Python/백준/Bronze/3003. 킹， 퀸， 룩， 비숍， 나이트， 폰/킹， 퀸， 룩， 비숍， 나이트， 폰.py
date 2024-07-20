tobe = [1,1,2,2,2,8]
asis = list(map(int,input().split())) 
result = []

for a, b in zip(tobe,asis):
    result.append((a-b))

print(' '.join(map(str,result)))