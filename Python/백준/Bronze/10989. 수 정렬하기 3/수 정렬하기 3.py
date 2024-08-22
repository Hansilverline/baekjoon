import sys

n = int(sys.stdin.readline())
n_list = [0]* 10001

for i in range(n):
    num = int(sys.stdin.readline())
    n_list[num] += 1 

for index,value in enumerate(n_list):
    if value != 0 :
        for _ in range(value):
            print(index)