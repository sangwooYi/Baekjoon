import sys
sys.stdin = open("baek2583.txt")


class Queue:
    
    def __init__(self, capactiy):
        self.max = capactiy
        self.que = [0] * self.max
        self.front = 0
        self.rear = 0 
        self.data = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.rear += 1
        self.data += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.front += 1
        self.data -= 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def is_empty(self):
        return self.data <= 0


def bfs(start_row, start_col):

    visited[start_row][start_col] = True

    que = Queue(M*N*2)
    que.enqueue((start_row, start_col))

    res = 1
    while not que.is_empty():

        row, col = que.dequeue()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            res += 1
            que.enqueue((next_row, next_col))
    return res

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
M, N, K = map(int, input().split())
visited = [[False] * M for _ in range(0, N)]

for i in range(0, K):
    x1, y1, x2, y2 = map(int, input().split())

    for row in range(x1, x2):
        for col in range(y1, y2):
            visited[row][col] = True

answer_arr = []
cnt = 0
for row in range(0, N):
    for col in range(0, M):
        if not visited[row][col]:
            cnt += 1
            area = bfs(row, col)
            answer_arr.append(area)

answer_arr.sort()

print(cnt)
print(" ".join(map(str, answer_arr)))