import sys
sys.stdin = open("baek2602.txt")

"""
이게 DP!!

아래처럼 혼자서 생각 할 수 있어야 한다 ㅠㅠ
"""



PAT = list(input())
DEV = list(input())
ANG = list(input())

path = len(DEV)
# DP[a][b][c]  a는 0 또는 1 악마인지 천사인지 돌다리 위치, b는 다리 위치 c는 현재까지 문자 위치
DP = [[[0] * len(PAT) for _ in range(0, len(DEV))] for _ in range(0, 2)]

# 첫글자 세팅?
for i in range(0, path):
    if DEV[i] == PAT[0]:
        DP[0][i][0] = 1
    if ANG[i] == PAT[0]:
        DP[1][i][0] = 1

for i in range(1, len(PAT)):
    for j in range(0, path):
        # 악마의길 j번째 글자가 패턴 i번째와 같을 때
        if DEV[j] == PAT[i]:
            for k in range(0, j):
                # 0 ~ j까지 중에서 천사의 길에서 패턴 i-1번째까지 완성된 경우
                DP[0][j][i] += DP[1][k][i-1]
        # 천사의 길도 동일
        if ANG[j] == PAT[i]:
            for k in range(0, j):
                DP[1][j][i] += DP[0][k][i-1]

answer = 0
for i in range(0, path):
    # 끝까지 전부 만든 경우 전부 합한다.
    answer += DP[0][i][len(PAT)-1]
    answer += DP[1][i][len(PAT)-1]
print(answer)
