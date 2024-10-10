import sys
import string

# 줄의 갯수가 정해져있지 않으므로 read로 한번에 받기
input = sys.stdin.read
# 개행문자와 공백을 제거하고 모든 글자를 하나의 문자열로 변환
lines = input().replace('\n', '').replace(' ', '')

# 알파벳 소문자를 키로 하는 딕셔너리 초기화
alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}

# 각 글자를 확인하여 카운트 증가
for char in lines:
    if char in alphabet_dict:  # 키가 존재할 경우
        alphabet_dict[char] += 1

# 가장 많이 나온 글자의 최대 카운트 찾기
max_count = max(alphabet_dict.values())

# 최대 카운트를 가진 모든 키 찾기
max_keys = [key for key, value in alphabet_dict.items() if value == max_count]

# 결과 출력 (공백 없이 출력)
print(''.join(max_keys))
