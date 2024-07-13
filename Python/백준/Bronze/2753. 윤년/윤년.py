isyoonyeon = int(input())
if isyoonyeon%4 == 0 and isyoonyeon%100 != 0 or isyoonyeon %400 == 0:
    print('1')
else :
    print('0')