import sys
sys.stdin = open("baek18405.txt")

"""
낮은 번호부터 증식시키는것과 동일한 효과를 위해

BFS 진행
=> 단 현재 경과 시간을 저장
퍼져나가려는 곳에 이미 존재하는 바이러스가 있다면
경과시간이 현재 경과시간보다 낮은값이면 => 무조건 pass
근데, 현재 경과시간과 같은 값이라면 => 둘 중 작은값이 적용 된다.

경과시간을 S초까지만 BFS 진행
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


def infested(arr, req_time, r, c):
    
    # 요구 시간이 0초면 바로 return
    if req_time == 0:
        return arr[r][c]

    size = len(arr)
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[-1] * size for _ in range(0, size)]
    que = Queue(size*size*100)

    for i in range(0, size):
        for j in range(0, size):
            if arr[i][j]:
                # 행, 열, 번호, 경과시간
                que.enqueue((i, j, arr[i][j], 0))
                visited[i][j] = 0
            
    while not que.is_empty():
        row, col, num, time = que.dequeue()

        # 현재시간 == 요구시간이면 진행 종료
        if time == req_time:
            continue
        next_time = time+1
        for k in range(0, 4):
            next_row = row + dr[k]
            next_col = col + dc[k]

            if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                continue
            # 현재 요구시간보다 낮은 값일때는 무조건 pass, 단 -1 아닌 때만(-1이면 아직 미방문이므로)         
            if visited[next_row][next_col] != -1 and visited[next_row][next_col] < next_time:
                continue

            # 같은 값일때는 현재 번호가 더 높은값이라면 pass (단 0이면 안됨)
            if arr[next_row][next_col] > 0 and arr[next_row][next_col] < num:
                continue
            # 진행
            visited[next_row][next_col] = next_time
            arr[next_row][next_col] = num
            que.enqueue((next_row, next_col, num, next_time))
    return arr[r][c]

N, K = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
S, Y, K = map(int, input().split())

# 인덱스로 조회해야하므로 Y, K 는 1씩조정
answer = infested(MAP, S, Y-1, K-1)

print(answer)