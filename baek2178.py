import sys
sys.stdin = open("baek2178.txt")


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


def bfs(maps, r, c):
    visited = [[False] * c for _ in range(0, r)]
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = Queue(r*c)
    visited[0][0] = True
    que.enqueue((0, 0, 1))
    while not que.isEmpty():
        now = que.dequeue()
        row = now[0]
        col = now[1]
        path = now[2]
        for dir in range(0, 4):
            next_row = row + dr[dir]
            next_col = col + dc[dir]
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            if visited[next_row][next_col]:
                continue
            if maps[next_row][next_col] == 0:
                continue
            visited[next_row][next_col] = True
            if (next_row == r-1) and (next_col == c-1):
                return path+1
            que.enqueue((next_row, next_col, path+1))


N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))
ans = bfs(MAP, N, M)
print(ans)