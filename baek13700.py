import sys
from collections import deque
sys.stdin = open("baek13700.txt")


def bfs():
    visited = [False] * (N+1)
    visited[S] = True

    for police in police_positions:
        visited[police] = True
    
    que = deque()
    que.append((S, 0))

    while que:
        cur_pos, cnt = que.popleft()    

        for d in range(0, 2):
            # 앞으로
            if d == 0:
                next_pos = cur_pos + F
            # 뒤로
            else:
                next_pos = cur_pos - B
            if next_pos <= 0 or next_pos > N:
                continue
            if visited[next_pos]:
                continue
            if next_pos == D:
                return cnt+1
            visited[next_pos] = True
            que.append((next_pos, cnt+1))
    return "BUG FOUND"

# N 건물의 갯수, S 출발지점, D 도착지점, F 앞으로 가는거리, B 뒤로가는 거리 K 경찰서 갯수
N, S ,D, F ,B, K = map(int, sys.stdin.readline().split())
police_positions = list(map(int, sys.stdin.readline().split()))

answer = bfs()
print(answer)