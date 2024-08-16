n = int(input())
result,count = 0,0
old_n = n
new_n = 0

if n == 0 :
    count = 1
while(new_n != n) :
    if old_n < 10 : 
        result = 0+old_n
    else :
        result = (old_n//10) + (old_n%10)
    new_n = (old_n%10) * 10 + (result%10)
    count += 1
    old_n=new_n

print(count)