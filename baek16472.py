import sys
sys.stdin = open("baek16472.txt")



alph_dict = {}

for i in range(0, 26):
    now = ord("a")
    alph_dict[chr(now+i)] = 0



N = int(input())
input_strings = input()

# 최대길이
max_len = 1
tmp_len = 1
# 알파벳 종류
alph_kind = 1
left = 0
right = 0
alph_dict[input_strings[0]] += 1

while left <= right and right < len(input_strings)-1:
    next_alph = input_strings[right+1]
    prev_alph = input_strings[left]

    next_kind = alph_kind
    # 다음 알파벳으로 들어오는 값이 현재 기준으로 없을때는 종류 추가
    if alph_dict[next_alph] == 0:
        next_kind += 1
    # right를 늘렸을 때 N종류가 넘어간다면 더이상 못늘림
    if next_kind > N:
        alph_dict[prev_alph] -= 1
        if alph_dict[prev_alph] == 0:
            alph_kind -= 1
        tmp_len -= 1
        left += 1
    else:
        alph_dict[next_alph] += 1
        alph_kind = next_kind
        tmp_len += 1
        right += 1
        max_len = max(max_len, tmp_len)
print(max_len)        
