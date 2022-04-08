import sys
sys.stdin = open("baek2602.txt")

"""
이게 DP 래 ㅡㅡ
일단 PASS
"""

def dfs(now, pos, is_dev, pat, devil, angel):
    global count
    
    # 종료 조건

    if len(now) == len(pat):
        if list(now) == pat:
            count += 1
        return
    
    for i in range(pos, len(devil)):
        if is_dev:
            if angel[i] in pat:
                dfs(now+angel[i], i, False, pat, devil, angel)
        else:
            if devil[i] in pat:
                dfs(now+devil[i], i, True, pat, devil, angel)


PAT = list(input())
DEV = list(input())
ANG = list(input())
count = 0
# 첫글자는 맞춰서 시작
flag = True
for i in range(0, len(DEV)):
    if DEV[i] == PAT[0]:
        start = i
        flag = False
        break
# 아예 첫글자부터 없는 경우
if flag:
    answer = 0
    print(answer)
else:
    dfs("", 0, False, PAT, DEV, ANG)
    print(count)