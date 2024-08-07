n, b = input().split()

ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n_list = list(n.upper())
total = 0 

for index,char_ in enumerate(reversed(n_list)) :
    total += int(b)**index * ary.index(char_)

print(total)
