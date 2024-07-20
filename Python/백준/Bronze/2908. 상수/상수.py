a, b = map(int,input().split())
str_a = [i for i in str(a)]
str_b = [i for i in str(b)]
str_a.reverse()
str_b.reverse()
re_a =int(''.join(str_a))
re_b =int(''.join(str_b))

print(max(re_a,re_b))