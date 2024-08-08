words = []
n = int(input())
for i in range(n):
    words.append(input())
set_words=set(words)

list_words = list(sorted(set_words, key=lambda x: (len(x),x)))
for i in list_words : 
    print(i)
