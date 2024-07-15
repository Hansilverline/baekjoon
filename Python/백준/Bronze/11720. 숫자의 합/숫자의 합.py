n = int(input())
string_number = input()
sum = 0
for i in range(n):
    sum += int(string_number[i:i+1])
print(sum)