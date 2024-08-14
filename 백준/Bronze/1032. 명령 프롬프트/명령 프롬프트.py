n = int(input())
file_name = []
for i in range(n) :
    file_name.append(input())
result = list(file_name[0]) # 죄초 기준문자열 

for i in range(1,n):
    for j in range(len(result)) :
        if file_name[i][j] == result[j] :
            pass
        else :
            result[j] = '?'

print(''.join(result))