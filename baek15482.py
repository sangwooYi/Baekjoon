import sys
# 한글 입력받으려면 encoding='utf-8' 조건을 반드시 추가해 주어야 함
sys.stdin = open("baek15482.txt", encoding='utf-8')

A = list(input())
B = list(input())

DP = [[0] * (len(B)+1) for _ in range(0, len(A)+1)]

# LCS 기본임! 반드시 기억해 두자
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[len(A)][len(B)])