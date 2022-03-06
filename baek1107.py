"""
경우 총 네 가지!
1. N .이 100인경우 => 무조건 0 반환

그 외엔
2. 일일이 하나씩 눌러 이동하는 경우
3. 찾아야하는 N값 기준 +으로 증가시키면서 가능한 숫자 찾기 
4. 찾야아하는 N값 기준 -으로 증가시키면서 가능한 숫자 찾기
2,3,4중 최솟값 반환

가능한 숫자 찾는 경우
현재 누르려는 숫자에서 불가능한 key가 있는지 체크해야함
현재 위치는 100 이것도 활용해야함!

EOF에러는 입출력 에러임!! 참고!!@
"""

import sys
sys.stdin = open("baek1107.txt")


def find_min(n, arrs):
    if n == 100:
        return 0
    case1 = abs(n - 100)
    case2 = 9999999
    case3 = 9999999

    pos_num = n
    neg_num = n
    chance = 0
    while True:
        if chance >= case1:
            break
        flag = True
        now = str(pos_num)
        for i in range(0, len(arrs)):
            if str(arrs[i]) in now:
                flag = False
                break
        if flag:
            case2 = len(now) + pos_num - n
            break 
        else:
            chance += 1
            pos_num += 1
    min = case1
    if min >= case2:
        min = case2

    chance = 0
    while True:
        if chance >= min:
            break
        flag = True
        now = str(neg_num)
        for i in range(0, len(arrs)):
            if str(arrs[i]) in now:
                flag = False
                break
        if flag:
            case3 = len(now) + n - neg_num
            break
        else:
            chance += 1
            neg_num -= 1

    if min >= case3:
        min = case3

    return min

N = int(input())
M = int(input()) 
# 고장난 버튼이 없으면 안주어짐 ... 문제 잘읽자!
brokens = []
if M > 0:
    brokens = list(map(int, input().split()))

answer = find_min(N, brokens)
print(answer)