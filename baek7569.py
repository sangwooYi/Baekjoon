import sys
sys.stdin = open("baek7569.txt")
"""
말그대로 3 차원 리스트로 풀자
r, c, h 로 풀면 된다.
상, 하, 좌, 우, 위, 아래
1은 익은토마토 0은 익지 않은것
-1은 빈칸(여긴 벽인것)
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


def tomato(box, h, r, c):
    # 위, 아래, 상, 하, 좌, 우 (델타함수 익숙해지자!)
    dh = [1, -1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]
    dr = [0, 0, 0, 0, -1, 1]

    que = Queue(r*c*h)
    # 토마토가 익으면 0 -> 1로 바꾸어주면 되므로 굳이 visited 쓸필요 X
    # 재귀로 진행안하기에 굳이 문제가 될 일은 없다.

    # 전부 1인상황 체크
    flag = True
    for height in range(0, h):
        for row in range(0, r):
            for col in range(0, c):
                # 0이 하나라도 나오면 flag 변경
                if box[height][row][col] == 0:
                    flag = False
                    continue
                # 1이 나올때는 que에 엔큐 해준다.
                elif box[height][row][col] == 1:
                    que.enqueue((height, row, col, 0))
    if flag:
        return 0

    while not que.isEmpty():
        now = que.dequeue()
        now_h = now[0]
        now_r = now[1]
        now_c = now[2]
        day = now[3]

        for dir in range(0, 6):
            next_h = now_h + dh[dir]
            next_r = now_r + dr[dir]
            next_c = now_c + dc[dir]
            
            # 맵 밖
            if next_h < 0 or next_r < 0 or next_c < 0 or next_h >= h or next_r  >= r or next_c >= c:
                continue
            # 빈칸
            if box[next_h][next_r][next_c] == -1:
                continue
            # 위에서 -1인 조건은 이미 제낌
            # 이미 익음 
            if box[next_h][next_r][next_c] > 0:
                continue
            # 익은걸로 바꾸고 엔큐
            # path 를 저장하는 방법으로
            box[next_h][next_r][next_c] = 1 + day
            que.enqueue((next_h, next_r, next_c, day+1))
    
    max_day = 0
    for height in range(0, h):
        for row in range(0, r):
            for col in range(0, c):
                # 안익은 토마토가 남아있으면 불가능한거 -1 반환
                if box[height][row][col] == 0:
                    return -1
                if box[height][row][col] == -1:
                    continue
                now_day = box[height][row][col]
                if now_day >= max_day:
                    max_day = now_day
    return max_day

           

# 가로(column) 세로(row)  높이 (height)
# 인덱스로는 [h][r][c] 이렇게 저장됨
M, N, H = map(int, input().split())
MAP = [0] * H
for i in range(0, H):
    box = [0] * N
    for j in range(0, N):
        temp = list(map(int, input().split()))
        box[j] = temp
    MAP[i] = box

ans = tomato(MAP, H, N, M)
print(ans)