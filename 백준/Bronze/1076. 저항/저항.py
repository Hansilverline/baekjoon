color = {'black':1,'brown':10,'red':100,'orange':1000,'yellow':10000,'green':100000,'blue':1000000,'violet':10000000,'grey':100000000,'white':1000000000}

index_list = list(color.keys())

color_1 = input()
num1 = index_list.index(color_1)

color_2 = input()
num2 = index_list.index(color_2)

color_3 = input()
mul = color[color_3]

print(int(str(num1)+str(num2))*mul)