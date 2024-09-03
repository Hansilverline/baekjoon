n = int(input())
f = int(input())

start = n - (n%100)
for i in range(start,start+100):
    if i % f == 0 :
        print(str(i)[-2:])
        break