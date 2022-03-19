import sys
sys.stdin = open("baek4179.txt")

"""
DFS 는 절대 안되고 (행, 열이 1000까지면 왠만하면 DFS는 아니다.),
BFS 응용문제!

BFS 를 한턴씩 돌려야 하는경우, 아래처럼 하면된다! 
이론을 알고있으면 충분히 응용 가능한 문제!
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
        return self.data <= 0  # 이렇게 bool형 판단식을 return하면 T/F값이 반환된다.


def findMinTime(maps, r, c):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * C for _ in range(0, R)]
    # 불은 따로 visited 써야할듯..
    f_visited = [[False] * C for _ in range(0, R)]
    # 불의 이동을 위한 큐
    f_q = Queue(r*c)
    # 지훈의 이동을 위한 큐
    j_q = Queue(r*c)  
    for row in range(0, r):
        for col in range(0, c):
            if maps[row][col] == "J":
                # 거리까지 저장
                j_start = (row, col, 0)
                j_q.enqueue(j_start)
                visited[row][col] = True
            elif maps[row][col] == "F":
                # 불은 여러개 존재할 수 있다 ...
                f_q.enqueue((row, col, 0))
                f_visited[row][col] = True
    
    while True:
        temp = []
        # 불을 먼저 한턴 돌리기
        while not f_q.isEmpty():
            now = f_q.dequeue()
            row = now[0]
            col = now[1]
            path = now[2]
            for dir in range(0, 4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if f_visited[next_row][next_col]:
                    continue
                if maps[next_row][next_col] == "#":
                    continue
                f_visited[next_row][next_col] = True
                temp.append((next_row, next_col, path+1))
        # 서로 한턴씩움직여야 한다 .. 이부분 조심
        for i in range(0, len(temp)):
            f_q.enqueue(temp[i])
 
        temp = []
        while not j_q.isEmpty():
            j_now = j_q.dequeue()
            j_row = j_now[0]
            j_col = j_now[1]
            j_path = j_now[2]
            if j_now == 0 or j_col == 0 or j_row == (r-1) or j_col == (c-1):
                return j_path + 1
            for dir in range(0, 4):
                j_next_row = j_row + dr[dir]
                j_next_col = j_col + dc[dir]
                next_path = j_path + 1
                if j_next_row < 0 or j_next_col < 0 or j_next_row >= r or j_next_col >= c:
                    continue
                if f_visited[j_next_row][j_next_col]:
                    continue
                if visited[j_next_row][j_next_col]:
                    continue
                if maps[j_next_row][j_next_col] == "#":
                    continue

                visited[j_next_row][j_next_col] = True
                temp.append((j_next_row, j_next_col, next_path))
        # 더이상 갈곳이 없는 경우 탈출 불가
        if len(temp) == 0:
            break
        for i in range(0, len(temp)):
            j_q.enqueue(temp[i])
 
    return "IMPOSSIBLE"

R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())
ans = findMinTime(MAP, R, C)
print(ans)