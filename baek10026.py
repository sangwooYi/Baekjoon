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



def RGB(arr, n):
    que = Queue(n*n)
    visited = [[False] * n for _ in range(0, n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que.enqueue((0, 0))
    visited[0][0] = True    
    count = 1
    while True:
        while not que.isEmpty():
            now = que.dequeue()
            n_row = now[0]
            n_col = now[1]
            for dir in range(0, 4):
                next_row = n_row + dr[dir]
                next_col = n_col + dc[dir]
                # 영역 밖 pass
                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                    continue
                # 이미 방문할떄 pass
                if visited[next_row][next_col]:
                    continue
                # 현재 탐색하려는 색과 다르면 pass
                if arr[n_row][n_col] != arr[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                que.enqueue((next_row, next_col))
        flag = True
        for row in range(0, n):
            if not flag:
                break
            for col in range(0, n):
                if not visited[row][col]:
                    flag = False
                    que.enqueue((row, col))
                    visited[row][col] = True
                    count += 1
                    break
        if flag:
            return count


N = int(input())
MAP = [0] * N
# 적록색맹용
MAP2 = [[0] * N for _ in range(0, N)]
for i in range(0, N):
    temp = list(input())
    MAP[i] = temp

for row in range(0, N):
    for col in range(0, N):
        if MAP[row][col] == "G":
            MAP2[row][col] = "R"
        else:
            MAP2[row][col] = MAP[row][col]

ans1 = RGB(MAP, N)
ans2 = RGB(MAP2, N)
print(f"{ans1} {ans2}")