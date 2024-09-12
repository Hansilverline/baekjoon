bin_1, bin_2 = input().split()

result = int(bin_1,2) + int(bin_2,2) # 10진수로 변환해서 더하기

print(bin(result)[2:])