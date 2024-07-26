str_= []

for i in range(5) :
    str_.append(input())


for i in range(15):
    for j in str_:
        try:
            print(j[i], end='')
        except IndexError:
            pass