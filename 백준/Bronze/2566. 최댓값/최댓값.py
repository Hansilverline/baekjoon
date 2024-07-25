matrix_ = [[0 for i in range(9)] for j in range(9)] # 행렬 초기화

for i in range(len(matrix_)) :
    matrix_[i] = list(map(int,input().split()))

max,row,col = 0,0,0

for i in range(len(matrix_)) :
    for j in range(len(matrix_[0])) :
        if matrix_[i][j] > max :
            max = matrix_[i][j]
            row = i
            col = j


print(max)
print(row+1,col+1)