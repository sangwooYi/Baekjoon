import sys
from collections import deque
sys.stdin = open("baek15573.txt")


# 주어진 K개 이상 캘 수 있는지 여부만 체크
def is_satisfied(drill_strength):


    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = 0
    visited = [[False] * (M) for _ in range(0, N)]
    que = deque()

    # 그냥 초반에 가능한 애들 전부 큐에저장하고 bfs 돌리면 된다.
    # bfs에서 나온 블록과 인접한애들은 어차피 최소한 한쪽이 공기에 닿아있는것!
    for i in range(0, M):
        if MAP[0][i] <= drill_strength:
            visited[0][i] = True
            que.append((0, i))
            cnt += 1
    for i in range(1, N):
        if MAP[i][0] <= drill_strength:
            visited[i][0] = True
            que.append((i, 0))
            cnt += 1
        if MAP[i][M-1] <= drill_strength:
            visited[i][M-1] = True
            que.append((i, M-1))
            cnt += 1
    if cnt >= K:
        return True

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]
            
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] <= drill_strength:
                visited[next_row][next_col] = True
                cnt += 1
                if cnt >= K:
                    return True
                que.append((next_row, next_col))
    if cnt >= K:
        return True
    return False 


def binary_search_left():

    left = 1
    right = 1000000

    while left < right:
        mid = (left+right)//2

        # 현재조건으로 만족하면 범위 줄이고
        if is_satisfied(mid):
            right = mid
        # 불가능하면 범위를 늘린다.
        else:
            left = mid+1
    return left

N, M, K = map(int, sys.stdin.readline().split())
# 공기층을 표현하기위해 buffer 요소를 둔다.
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

answer = binary_search_left()
print(answer)