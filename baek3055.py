import sys
sys.stdin = open("baek3055.txt")

"""
턴제로 탐색해야함!
물을 먼저 흘려 보낸뒤에,
고슴도치가 갈 수 있는 경로를 파악
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

    def is_empty(self):
        return self.data <= 0


def find_min_time(arr):
    r = len(arr)
    c = len(arr[0])
    visited = [[False] * c for _ in range(0, r)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    main_que = Queue(r*c*5)
    water_que = Queue(r*c*5)

    water = "*"
    stone = "X"
    destination = "D"
    for row in range(0, r):
        for col in range(0, c):
            if arr[row][col] == "S":
                start_row = row
                start_col = col
                visited[start_row][start_col] = True
                main_que.enqueue((start_row, start_col, 0))
            elif arr[row][col] == water:
                water_que.enqueue((row, col))

    while not main_que.is_empty():
        tmp_que = Queue(r*c)
        while not water_que.is_empty():
            row, col = water_que.dequeue()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if arr[next_row][next_col] == stone:
                    continue
                if arr[next_row][next_col] == destination:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                arr[next_row][next_col] = water
                tmp_que.enqueue((next_row, next_col))
        while not tmp_que.is_empty():
            row, col = tmp_que.dequeue()
            water_que.enqueue((row, col))
        
        while not main_que.is_empty():
            row, col, time = main_que.dequeue()

            next_time = time+1
            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if arr[next_row][next_col] == destination:
                    return next_time
                if arr[next_row][next_col] == water:
                    continue
                if arr[next_row][next_col] == stone:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                tmp_que.enqueue((next_row, next_col, next_time))
                
        while not tmp_que.is_empty():
            row, col, time = tmp_que.dequeue()
            main_que.enqueue((row, col, time))        
    
    return "KAKTUS"

R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())


answer = find_min_time(MAP)
print(answer)