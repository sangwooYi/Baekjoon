import sys
sys.stdin = open("baek14722.txt")

"""
무조건 0번 우유 -> 1번우유 -> 2번우유 -> 0번우유 순으로 마셔야함

DP[row][col][num] 
row, col 지점까지 num 번 우유를 마지막로 먹을때 최대 갯수

이런 문제 풀줄 알아야 한다.
핵심은 왼쪽, 윗쪽 값에서 마지막으로 채택한 우유가 무엇인지를 저장하고 있어야한다는것!
따라서 현재까지의 우유 누적합, 마지막으로 채택한 우유를 계속 체크하면서
DP를 진행하는게 핵심 아이디어!
"""



N = int(input())
MAP = [0] * N

for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
# [row][col][0]은 row, col 까지 누적합 / [row][col][1]은 row, col 에서 채택한 마지막 우유
DP = [[[0, -1] for _ in range(0, N+1)] for _ in range(0, N+1)]


for row in range(1, N+1):
    for col in range(1, N+1):
        left = DP[row][col-1]
        up = DP[row-1][col]

        if (left[1]+1)%3 == MAP[row-1][col-1]:
            left_check = 1
        else:
            left_check = 0
        
        if (up[1]+1)%3 == MAP[row-1][col-1]:
            up_check = 1
        else:
            up_check = 0
        
        left_sum = left[0]+left_check
        up_sum = up[0] + up_check

        if left_sum > up_sum:
            DP[row][col][0] = left_sum
            if left_check:
                DP[row][col][1] = MAP[row-1][col-1]
            else:
                DP[row][col][1] = left[1]
        
        else:
            DP[row][col][0] = up_sum
            if up_check:
                DP[row][col][1] = MAP[row-1][col-1]
            else:
                DP[row][col][1] = up[1]
print(DP[N][N][0])