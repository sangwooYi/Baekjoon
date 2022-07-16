import sys
sys.stdin = open("baek5582.txt")

"""
LCS (Longest Common Subsequence) 와 구문하자, 
LCS는 연속되지 않아도 된다! 
이문제는 연속되야함! (그냥 Common Subsequence 문제)
DP[i][j] 는 첫번째문자 i번, 두번째문자 j번 까지에서의 공통 부분 문자열길이
"""


string1 = list(input())
string2 = list(input())
n = len(string1)
m = len(string2)

# 0번째인덱스는 여유칸으로
DP = [[0] * (m+1) for _ in range(0, n+1)]

# 연속되야하면 이렇게
answer = 0
for i in range(0, n):
    for j in range(0, m):
        if string1[i] == string2[j]:
            DP[i+1][j+1] = DP[i][j] + 1
            # 그냥 매번 갱신하는 형태로!
            answer = max(DP[i+1][j+1], answer)
print(answer)


# 이 방법은 연속되지 않아도 되는것! (LCS)
# for i in range(0, n):
#     for j in range(0, m):
#         # 현재 문자열이 같은경우
#         if string1[i] == string2[j]:
#             DP[i+1][j+1] = DP[i][j] + 1
#         # 다른 경우
#         else:
#             DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])