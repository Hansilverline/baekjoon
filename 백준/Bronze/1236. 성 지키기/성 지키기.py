from sys import stdin

# n: 행의 개수, m: 열의 개수
n, m = map(int, stdin.readline().split())

# 성의 상태를 저장할 2차원 리스트 arr
arr = []

# 각 열에 'X'가 있는지를 기록할 리스트 col (False로 초기화)
# 각 행에 'X'가 있는지를 기록할 리스트 row (False로 초기화)
col = [False] * m
row = [False] * n

# 'X'가 없는 행의 수를 저장할 변수 r1
# 'X'가 없는 열의 수를 저장할 변수 r2
r1, r2 = 0, 0

# 성의 상태를 입력받아 arr 리스트에 저장
for i in range(n):
    data = list(stdin.readline().rstrip())  # 각 행을 입력받아 리스트로 변환
    arr.append(data)  # 변환된 리스트를 arr에 추가

# 성의 상태를 조사하여 각 행(row)과 열(col)에 'X'가 있는지 기록
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':  # 해당 위치에 'X'가 있으면
            row[i] = True     # 해당 행에 'X'가 있음을 표시
            col[j] = True     # 해당 열에 'X'가 있음을 표시

# 'X'가 없는 행의 개수를 셈
for i in range(n):
    if not row[i]:  # 해당 행에 'X'가 없으면
        r1 += 1     # r1을 1 증가시킴

# 'X'가 없는 열의 개수를 셈
for j in range(m):
    if not col[j]:  # 해당 열에 'X'가 없으면
        r2 += 1     # r2을 1 증가시킴

# r1(빈 행의 수)과 r2(빈 열의 수) 중 큰 값을 출력
print(max(r1, r2))
