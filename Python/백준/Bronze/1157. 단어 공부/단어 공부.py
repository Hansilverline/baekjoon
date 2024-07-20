word = input().upper()
word_set_list = list(set(word))
count = []
for i in word_set_list :
    count.append((i,word.count(i)))
maxs = []
for i in count : 
    if i[1] == max(count, key=lambda x: x[1])[1] :
        maxs.append(i)
if len(maxs) == 1 :
    print(maxs[0][0])
else :  
    print("?")