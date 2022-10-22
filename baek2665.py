import sys
from collections import deque
sys.stdin = open("baek2665.txt")



"""
DP[a][b]
=> a,b 좌표까지 가는데 부순 최소 벽의 갯수를 저장!
이게 더 큰경우는 진행할 필요 X
다익스트라는 원래 힙큐를 사용!
근데 이 문제에서는 가중치가 같으므로 그냥 큐를 쓴것!
다음 갈 방이 길이면 (1)
그냥 DP[next_node] > DP[node] 인 경우 갱신,
다음 갈 방이 벽이면 (0)
 DP[next_node] > DP[node]+1 인 경우만 갱신
"""

def dijkstra(arr):
    n = len(arr)
    INF = 987654321
    DP = [[INF] * n for _ in range(0, n)]
    DP[0][0] = 0
    que = deque()
    que.append((0, 0))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                continue
            # 길
            if arr[next_row][next_col]:
                # 더 적은 경로일때만 갱신
                if DP[next_row][next_col] > DP[row][col]:
                    DP[next_row][next_col] = DP[row][col]
                    que.append((next_row, next_col))
            # 벽
            else:
                # 벽을 깨부시고 가도, 더 적은 벽인 갯수일떄만
                if DP[next_row][next_col] > DP[row][col]+1:
                    DP[next_row][next_col] = DP[row][col]+1
                    que.append((next_row, next_col))
    return DP[n-1][n-1]
    


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))

answer = dijkstra(MAP)
print(answer)