s = input()
alphabet_list = [chr(i) for i in range(97,123)]
count_list = []

for i in alphabet_list :
    if i in s :
        count_list.append(s.index(i))
    elif i not in s :
        count_list.append(-1)
    
for i in count_list :
    print(i,end = ' ')