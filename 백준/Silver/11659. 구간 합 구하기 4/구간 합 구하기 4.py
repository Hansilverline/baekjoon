import sys
input = sys.stdin.readline 

n, m = map(int, input().split()) # 개수, 합
nums = list(map(int, input().split()))
total = 0 # 각 수의 합 저장
prefixSum = [0] # 구간합 저장 리스트 

for i in nums:    
    total += i    
    prefixSum.append(total) 

for _ in range(m):    
    i, j = map(int, input().split())    
    print(prefixSum[j] - prefixSum[i - 1])