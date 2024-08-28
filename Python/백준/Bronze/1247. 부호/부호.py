import sys

for _ in range(3):
    set_num = int(sys.stdin.readline())
    list_ = [0 for _ in range(set_num)]
    for i in range(set_num):
        list_[i] = int(sys.stdin.readline()) 

    if sum(list_) == 0 :
        print(0)
    elif sum(list_) > 0 :
        print('+')
    else :
        print('-')