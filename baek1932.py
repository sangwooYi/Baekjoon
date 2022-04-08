import sys
sys.stdin = open("baek1932.txt")

"""
이동방향은
# 이렇게밖에 못움직인다!
dr = [1, 1]
dc = [0, 1]

# 물론 i-1, j-1 /  i-1, j 가 맵 밖인 경우는 제외
DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]) + MAP[i][j]
"""

def max_path(arr, n):
    DP = [[0] * i for i in range(1, n+1)]
    DP[0][0] = arr[0][0]
    if n == 1:
        return DP[0][0]
    dr = [-1, -1]
    dc = [-1, 0]

    ans = 0 
    for row in range(1, n):
        for col in range(0, len(arr[row])):
            max_value = 0
            for dir in range(0, 2):
                past_row = row + dr[dir]
                past_col = col + dc[dir]
                # 사실상 row가 벗어날일은 없다.
                if past_col < 0 or past_col >= len(arr[row])-1:
                    continue
                if max_value < DP[past_row][past_col]:
                    max_value = DP[past_row][past_col]
            DP[row][col] = max_value + arr[row][col]
            if row == n-1 and ans < DP[row][col]:
                ans = DP[row][col]
    return ans

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

answer = max_path(MAP, N)
print(answer)