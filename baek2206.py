import sys
sys.setrecursionlimit(10**4)
sys.stdin = open("baek2206.txt")

"""
역시나 시간초과 ㅡㅡ
BFS ? DFS ?
BFS 로 구현하면 벽 깨는게 어딘지 어떻게 체크하는게 효율적일지? 

DFS + 가지치기는 해봤을때 시간 초과됨(너무 N, M이 크다.
(가로, 세로가 100 미마인경우만 DFS, 가지치기로 접근하고 이런문제는
진짜 왠만하면 BFS다!)

이방법으로 BFS 문제도 풀 수 있어야한다!
3차원 리스트로 선언하여 기회를 썼는지 안썻는지 체크하여 진행!
이 문제는 한번 더 풀어볼것!

BFS에 대해 이해가 완벽해야 풀 수 있는문제!
어차피 너비탐색이기에, 아래와같이 조건을 걸어도, 결국 가장 빠른 길로 갈 수 있는
path가 탐색되어 반환되는것!

"""

class Queue:
    
    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0

        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now

    def isEmpty(self):
        return self.data <= 0


def bfs(arr, n, m):
    que = Queue(n*m)
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[[0] * 2 for _ in range(0, M)] for _ in range(0, N)]
    que.enqueue((0, 0, 0))
    # 아직 안부셨으면 0으로 부셨으면 1로
    visited[0][0][0] = 1

    while not que.isEmpty():
        now = que.dequeue()
        now_row = now[0]
        now_col = now[1]
        chance = now[2]

        if now_row == n-1 and now_col == m-1:
            print(visited)
            # BFS이므로 최단경로에 값이 제일 먼저 여기에 도달한다
            return visited[now_row][now_col][chance]
        for dir in range(0, 4):
            next_row = now_row + dr[dir]
            next_col = now_col + dc[dir]
            # 맵 밖
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
                continue
            # 벽인데 아직 벽부수지 않은 경우
            if arr[next_row][next_col] == 1 and chance == 0:
                visited[next_row][next_col][1] = visited[now_row][now_col][0] + 1
                que.enqueue((next_row, next_col, 1))
            # 벽이 아니고 통과 가능
            elif arr[next_row][next_col] == 0 and visited[next_row][next_col][chance] == 0:
                visited[next_row][next_col][chance] = visited[now_row][now_col][chance] + 1
                que.enqueue((next_row, next_col, chance))
    return -1



N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    temp = list(map(int, input()))
    MAP[i] = temp

min_path = bfs(MAP, N, M)
# 벽이 있는 경우는 벽처리도 진행
# 이부분을 그냥 한번에 처리하는 로직으로 바꾸는게 핵심 idea임
print(min_path)


