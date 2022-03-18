import sys
sys.stdin = open("baek4179.txt")

"""
DFS 는 절대 안되고 (행, 열이 1000까지면 왠만하면 DFS는 아니다.),
BFS 응용문제
매초마다
불길 번지는 영역을 체크

그다음 지훈이 이동하려는 거리가 아직 불이 도달하기 직전인지를 판단!
아 그리고 불은 여러개 있다 ㅡㅡ

시간초과 야발 ㅡㅡ
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
    fire_forecast = {}
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * C for _ in range(0, R)]
    # 불의 이동을 위한 큐
    f_q = Queue(r*c)
    # 지훈의 이동을 위한 큐
    j_q = Queue(r*c)  
    for row in range(0, r):
        for col in range(0, c):
            if maps[row][col] == "J":
                # 거리까지 저장
                j_start = (row, col, 0)
            elif maps[row][col] == "F":
                # 불은 여러개 존재할 수 있다 ...
                f_q.enqueue((row, col, 0))
                if 0 in fire_forecast.keys():
                    fire_forecast[0].append([row, col])
                else:
                    fire_forecast[0] = [[row, col]]
                visited[row][col] = True
    while not f_q.isEmpty():
        f_now = f_q.dequeue()
        f_row = f_now[0]
        f_col = f_now[1]
        f_path = f_now[2]
        for dir in range(0, 4):
            next_row = f_row + dr[dir]
            next_col = f_col + dc[dir]
            # 영역 밖 pass
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            # 이미 방문 pass
            if visited[next_row][next_col]:
                continue
            # 벽이면 pass
            if maps[next_row][next_col] == "#":
                continue
            visited[next_row][next_col] = True
            f_q.enqueue((next_row, next_col, f_path+1))
            if (f_path+1) in fire_forecast.keys():
                fire_forecast[f_path+1].append([next_row, next_col])
            else:
                fire_forecast[f_path+1] = [[next_row, next_col]]

    # 지훈이가 이동하기 위해 visited 초기화
    # 그 후 매 path에 맞게 불길 visited 체크
    visited = [[False] * C for _ in range(0, R)]
    visited[j_start[0]][j_start[1]] = True
    fire_start = fire_forecast[0]
    for i in range(0, len(fire_start)):
        visited[fire_start[i][0]][fire_start[i][1]] = True
    j_q.enqueue(j_start)
    while not j_q.isEmpty():
        now = j_q.dequeue()
        row = now[0]
        col = now[1]
        path = now[2]
        if path+1 in fire_forecast.keys():
            fire = fire_forecast[path+1]
            for i in range(0, len(fire)):
                # 현재 path 기준 다음 갈 길에 불길이 번져있는곳을 체크
                visited[fire[i][0]][fire[i][1]] = True
        for dir in range(0, 4):
            next_row = row + dr[dir]
            next_col = col + dc[dir]
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            if visited[next_row][next_col]:
                continue
            if maps[next_row][next_col] == "#":
                continue
            # 경계선에 도달한것, 탈출조건은 1초후
            if next_row == 0 or next_col == 0 or next_row == r-1 or next_col == c-1:
                return (path+2)
            visited[next_row][next_col] = True
            j_q.enqueue((next_row, next_col, path+1))
    # 위 while문을 지나왔으면 탈출 불가능한것
    return "IMPOSSIBLE"


R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())
ans = findMinTime(MAP, R, C)
print(ans)