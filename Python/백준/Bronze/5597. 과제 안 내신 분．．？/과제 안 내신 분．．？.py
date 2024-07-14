students = []
for a in range(30):
    students.append(0)
for i in range(28):
    n = int(input())
    students[n-1] = n
first = students.index(0)+1
second = students.index(0,first)+1
print(first,second,sep='\n')