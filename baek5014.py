import sys
sys.stdin = open("baek5014.txt")
from collections import deque


def is_range(cur):
    if cur <= 0 or cur > F:
        return False
    return True

def bfs():
    visited = [False] * (F+1)
    que = deque()
    visited[S] = True
    que.append((S, 0))

    UP = 0
    DOWN = 1
    while que:
        cur_floor, cnt = que.popleft()
        # 시간초과만 안난다면 현재 위치를 검사하자!
        if cur_floor == G:
            return cnt

        for i in range(0, 2):
            if i == UP:
                next_floor = cur_floor+U
            elif i == DOWN:
                next_floor = cur_floor-D
            
            if is_range(next_floor):
                if visited[next_floor]:
                    continue
                visited[next_floor] = True
                que.append((next_floor, cnt+1))
    return "use the stairs"


# F: 최대 / S: 현재 / G: 목표 / U: 위로 U칸이동 / D: 아래로 D칸 이동
F, S, G, U, D = map(int, input().split())
answer = bfs()
print(answer)