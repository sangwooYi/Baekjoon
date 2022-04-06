import sys
sys.stdin = open("baek18870.txt")
"""

"""


N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

check = {}
# 숫자 종류를 key, 각 인덱스값들을 value
for i in range(0, N):
    if X[i] in check.keys():
        check[X[i]].append(i)
    else:
        check[X[i]] = [i]
kind_num = list(check.keys())
# 주어진 숫자들의 종류만 받아와서 sort
kind_num.sort()
answer = [0] * N
# 각 숫자를 갖는 idx 위치를 value값으로 받아오므로, 그 위치에 해당 값 저장.
# 그냥 i번쨰로 오는 숫자는 자기보다 낮은애가 i개 존재하는것!
for i in range(0, len(kind_num)):
    loc = check[kind_num[i]]
    for idx in range(0, len(loc)):
        answer[loc[idx]] = i
for i in range(0, len(answer)):
    if i == len(answer)-1:
        print(answer[i])
    else:
        print(answer[i], end=" ")