import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek1937.txt")

"""
그냥 DFS 돌리면 무조건 시간초과.

이걸 줄이려면
=> 가지치기 / DP
여기선 DP.인데 
DP를 어떻게 적용할 수 있는지에 대해 떠올릴 수 있어야 한다.
아직 너무 부족하다...

DFS , 재귀 에서 DP 적용하는 방법 
=> 보통은 메모이제이션!!!!!
=> 떠올리는 TIP. 어떤 부분이 계속해서 호출되는지에대해 고민해보자.
=> 그 부분을 저장해두고 호출해서 재귀 호출 횟수를 확 줄이는게 POINT !!!

반드시 다시 풀어 보자!
꼭 다시 풀 문제!!
재귀, 너무 어렵다..
"""


# DP[i][j]  i, j 칸까지로의 최대 이동 경로
def dfs(arr, row, col):
    # 메모이제이션이 핵심! 이미 거쳐간 경로면 그대로 리턴
    if DP[row][col]:
        return DP[row][col]
    # 아니면 기본값이 1
    DP[row][col] = 1
    for i in range(0, 4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        # 범위 밖
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue
        # 다음지역이 더 많은 곳만 갈 수 있음
        if arr[next_row][next_col] <= arr[row][col]:
            continue
        # 현재 저장된 값 vs next_row, next_col에서 재귀돌렸을때 값+1
        # 여기서 dfs(arr, next_row, next_col)에서 만약 위의 
        # if DP[row][col]: return DP[row][col] 이 조건 없었으면 얘도 무조건 계속 재귀가 돌아 갈 것!
        # 메모이제이션!!!!!
        DP[row][col] = max(DP[row][col], dfs(arr, next_row, next_col)+1)

    # 더이상 갈 곳없으면  return
    return DP[row][col]


N = int(input())    
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
DP = [[0] * N for _ in range(0, N)]

answer = 0
# 시작점을 전부 돌려 보아야 한다.
for i in range(0, N):
    for j in range(0, N):
        # 여기서 dfs(MAP, i, j) 역시, 이미 가본 경로면 바로 return 됨
        answer = max(answer, dfs(MAP, i, j))

print(answer)

