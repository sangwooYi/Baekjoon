import sys
sys.stdin = open("baek6953.txt")


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



def bfs(arr, start):
    
    # 상 하 북 남 서 동
    dh = [1, -1, 0, 0, 0, 0]
    dr = [0, 0, -1, 1, 0, 0]
    dc = [0, 0, 0, 0, -1, 1]


    que = Queue(L*R*C*100)
    visited = [[[False] * C for _ in range(0, R)] for _ in range(0, L)]
    s_h, s_r, s_c = start
    visited[s_h][s_r][s_c] = True
    # 시작, 출구가 같은 경우는 없음
    que.enqueue((s_h, s_r, s_c, 0))
    
    while not que.is_empty():

        height, row, col, time = que.dequeue()
        
        for k in range(0, 6):
            next_height = height + dh[k]
            next_row = row + dr[k]
            next_col = col + dc[k]
            next_time = time+1
            if next_height < 0 or next_row < 0 or next_col < 0 or next_height >= L or next_row >= R or next_col >= C:
                continue
            if arr[next_height][next_row][next_col] == "#":
                continue
            if visited[next_height][next_row][next_col]:
                continue
            if arr[next_height][next_row][next_col] == "E":
                return next_time
            visited[next_height][next_row][next_col] = True
            que.enqueue((next_height, next_row, next_col, next_time))
    return -1
            



while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    MAP = [0] * L
    for i in range(0, L):
        temp = [0] * R
        for j in range(0, R+1):
            tmp = input()
            if j < R:
                temp[j] = list(tmp)
        MAP[L-1-i] = temp
    flag = False
    for h in range(0, L):
        if flag:
            break
        for r in range(0, R):
            if flag:
                break
            for c in range(0, C):
                if MAP[h][r][c] == "S":
                    flag = True
                    start_point = (h, r, c)
                    break

    answer = bfs(MAP, start_point)
    if answer == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {answer} minute(s).")