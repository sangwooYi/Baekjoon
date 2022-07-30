import re
import sys
sys.stdin = open("baek16172.txt")


"""
숫자 제거를 직접하면 시간 초과난다.
KMP 알고리즘은 익혀 둘 것!
"""

# 이 KMP 알고리즘 꼭 익혀 두자!
def kmp(text, pattern):

    pp = 0
    pt = 1
    pt_len = len(pattern)
    txt_len = len(text)
    skip = [0] * (pt_len+1)

    # skip 표 작성 
    while pt < pt_len:
        if pattern[pp] == pattern[pt]:
            pp += 1
            skip[pt] = pp
            pt += 1
        elif pp == 0:
            skip[pt] = pp
            pt += 1
        else:
            pp = skip[pp-1]

    pp = 0
    pt = 0
    while pt < txt_len and pp < pt_len:
        if text[pt] == pattern[pp]:
            pp += 1
            pt += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp-1]
    # 일치 확인
    if pp == pt_len:
        return 1
    return 0


S = input()
K = input()

# 파이썬에서 정규식 이용해서 문자열 치환하는방법!!! re 라이브러리 공부할 것
real_s = re.sub("[0-9]", "", S)

answer = kmp(real_s, K)
print(answer)