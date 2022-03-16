import sys
sys.stdin = open("baek10026.txt")

"""
적록색약은  R, G의 차이를 못느낀다.
DFS 보다는 BFS 너비탐색이 맞을 듯? 맞네!
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


def RGB(maps, n):
    count = 1
    que = Queue(n*n)
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(0, N)]
    start = (0, 0)
    visited[0][0] = True
    que.enqueue(start)
    while True:
        while not que.isEmpty():
            now = que.dequeue()
            now_row = now[0]
            now_col = now[1]
            now_color = maps[now_row][now_col]
            for dir in range(0, 4):
                next_row = now_row + dr[dir]
                next_col = now_col + dc[dir]
                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                    continue
                if visited[next_row][next_col]:
                    continue
                next = (next_row, next_col)
                next_color = maps[next_row][next_col]
                if next_color != now_color:
                    continue
                # 같은색인 경우만 gogo
                visited[next_row][next_col] = True
                que.enqueue(next)
        # 인접한 같은색깔을 전부 탐색한 후에 내부 while문 탈출
        flag = True
        for i in range(0, n):
            if not flag:
                break
            for j in range(0, n):
                if not visited[i][j]:
                    # 아직 방문안한곳 찾으면 다른영역인것
                    flag = False
                    que.enqueue((i, j))
                    visited[i][j] = True
                    break
        # 전부 돈 경우, 그냥 값 return
        if flag:
            return count
        count += 1


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

# 적록색맹용
MAP2 = [[0] * N for _ in range(0, N)]
for i in range(0, N):
    for j in range(0, N):
        if MAP[i][j] == "G":
            MAP2[i][j] = "R"
        else:
            MAP2[i][j] = MAP[i][j]

answer = RGB(MAP, N)
answer2 = RGB(MAP2, N)
print(answer, answer2)
