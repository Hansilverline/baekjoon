a,b = map(int,input().split())

num_list = []
for i in range(1,int(1000/2)):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[a-1:b]))