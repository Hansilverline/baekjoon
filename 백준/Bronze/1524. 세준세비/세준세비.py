import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
    input()
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())),reverse=True)
    m_list = sorted(list(map(int, input().split())),reverse=True)
    # print('n_list : ',n_list)
    # print('m_list : ',m_list)

    while n_list and m_list:
        # 최소값을 각각 저장
        min_n = n_list[-1]
        min_m = m_list[-1]

        # 리스트에서 최소값을 안전하게 제거
        if min_n < min_m:
            n_list.pop()
        else:
            m_list.pop()

    if n_list:
        print('S')  # 세준 승리
    elif m_list:
        print('B')  # 세비 승리
    else:
        print('C')  # 무승부
