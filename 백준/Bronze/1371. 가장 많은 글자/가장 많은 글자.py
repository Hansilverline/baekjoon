import sys
import string

# 줄의 갯수가 정해져있지 않음으로 read로 한번에 받기
input = sys.stdin.read
# 개행문자, 공백 제거
lines = input().replace('\n','').replace(' ','')

alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}

# 각 글자를 확인하여 카운트 증가
for char in lines:
    if char in alphabet_dict:  # 키가 존재할 경우
        alphabet_dict[char] += 1

max_count = max(alphabet_dict.values())

max_keys = [key for key, value in alphabet_dict.items() if value == max_count]

print(''.join(max_keys))