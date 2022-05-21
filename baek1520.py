import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek1520.txt")

"""
아이디어!

500 * 500 이므로 DFS로는 택도 없다.
20*20 이하면, DFS로도 비벼볼수 있을듯?

DFS / DP 같이 사용하는 문제임
꼭 익혀두자!

재귀함수 짜는 방법 익혀두어야한다!

기본적으로 아래 로직은,
일단 DFS로 갈수 있는 곳 까지진행하며,
그 후에, 스택이 해제되면서 22 / 25번의 return값이
적절하게 tmp 에 대입되게된다.

이문제 꼭 다시 풀어볼것!
아래코드가 내가 더 이해하기가 쉽다!
"""

def dfs(arr, visited, row, col, m, n):
    if row == m-1 and col == n-1:
        return 1
    if visited[row][col] == -1:
        visited[row][col] = 0
        for i in range(0, 4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n:
                continue
            if arr[next_row][next_col] >= arr[row][col]:
                continue
            # next_row, next_col 까지 몇가지 case가 이동 가능한지
            tmp = dfs(arr, visited, next_row, next_col, m, n)
            visited[row][col] += tmp

    # 위 for문이 끝나고 나서 거치게 될 부분
    return visited[row][col]


# 여기선 row(세로)가 M col(가로)이 N  
M, N = map(int, input().split())
MAP = [0] * M
for i in range(0, M):
    MAP[i] = list(map(int, input().split()))

# 상 좌 하 우, 해당 칸에 들어온 방향을 나타냄
DP = [[[0] * N for _ in range(0, M)] for _ in range(0, 4)]

# 상 좌 하 우 반전시 (dir+2) % 4 로 하기 위함
dr = [-1, 0, 1, 0] 
dc = [0, -1, 0, 1]

check = [[-1] * N for _ in range(0, M)]
print(dfs(MAP, check, 0, 0, M, N))
