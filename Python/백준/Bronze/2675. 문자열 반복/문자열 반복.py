t = int(input())

for i in range(t) :
    loop_count, s = input().split()
    for alphabet in s:
        print(alphabet*int(loop_count),end='')
    print()