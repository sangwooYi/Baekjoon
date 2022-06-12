import sys
sys.stdin = open("baek9252.txt")
"""
LCS는 꼭 기억!
얘는 길이대신 문자열을 저장
"""


a = list(input())
b = list(input())

# 문자열을 저장 DP[i][j] i행 j열 이전까지의 LCS를 나타냄
DP = [[""] * (len(b)+1) for _ in range(0, len(a)+1)]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        # 같은 경우
        if a[i] == b[j]:
            DP[i+1][j+1] = DP[i][j] + a[i]
        else:
            tmp1 = DP[i+1][j]
            tmp2 = DP[i][j+1]
            if len(tmp1) > len(tmp2):
                DP[i+1][j+1] = tmp1
            else:
                DP[i+1][j+1] = tmp2
answer = DP[len(a)][len(b)]
if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(answer)