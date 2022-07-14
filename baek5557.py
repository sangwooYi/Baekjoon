import sys
sys.stdin = open("baek5557.txt")

"""
핵심은 수가 0부터 20까지라는것! => 충분히 인덱스로 계산 가능
DP[i][j] => i번 인덱스까지 계산했을때 j가 나올 수 있는 경우의 수

제발 ... DP 좀 혼자 풀자..
"""


N = int(input())
nums = list(map(int, input().split()))

# 0부터 20까지
DP = [[0] * 21 for _ in range(0, N)]
# 초깃값
DP[0][nums[0]] = 1

for i in range(1, N-1):
    num = nums[i]
    for j in range(0, 21):
        # i-1 인덱스계산까지 j가 나온 경우

        # 합이 20 이하일 때 덧셈 가능
        if j + num <= 20:
            DP[i][j+num] += DP[i-1][j]
        # 뺄때 0 이상인 경우
        if j - num >= 0:
            DP[i][j-num] += DP[i-1][j]
# N-2 인덱스까지 진행했을때 N-1 인덱스의 값과 동일한 값이 나올 경우
print(DP[N-2][nums[N-1]])
