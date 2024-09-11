col, row = map(int,input().split())

castle = []

for i in range(col):
    castle.append(input())

col_cnt = 0 
row_cnt = 0

# 가로 방향으로 X가 없으면 추가하는 코드
for i in range(col):
    if 'X' not in castle[i] :
        row_cnt +=1

for j in range(row):
    if "X" not in [castle[i][j] for i in range(col)]:
        col_cnt += 1

print(max(row_cnt,col_cnt))