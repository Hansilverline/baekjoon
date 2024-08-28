x,y,w,h = map(int, input().split())

if w-x > x :
    x_min = x
else :
    x_min = w-x

if h-y > y:
    y_min = y
else :
    y_min = h-y

print(min(x_min, y_min))