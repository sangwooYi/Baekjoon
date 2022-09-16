import sys
sys.stdin = open("baek2636.txt")


"""
모든 1이 없어질때까지 아래 반복 진행

1. 우선 빈공간중 치즈 구멍인 부분을 체크, -1로 변경한다.
   => 0,0 (무조건 빈공간)에서 bfs 진행해서 체크 안된 0 부분이 치즈 구멍!

2. 모든 치즈를 순회할떄까지 진행하며, 
   해당 치즈가 한면이라도 공기랑 닿아있으면 2로 변경
   (근데 BFS 안해도 되지 않나..???)

3. 2에 해당하는 부분들을 제거하고 (0으로) -1인 부분도 다시 0으로 변경, 
   치즈가 없으면 종료, 아직 남아있으면 다시 1로 돌아감
"""

class Queue:

    def __init__(self, capactiy):
        self.max = capactiy
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
            self.max = 0
        return now
    
    def is_empty(self):
        return self.data <= 0


# (걸린 시간, 다녹기 직전 치즈갯수)를 반환
def req_time_cheese_clear(arr):
    r = len(arr)
    c = len(arr[0])
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    flag = False
    for row in range(0, r):
        if flag:
            break
        for col in range(0, c):
            if arr[row][col]:
                flag = True
                break
    if not flag:
        # 처음부터 아예 치즈가 없는 경우
        return (0, 0)
    time = 1
    while True:
        # 치즈 구멍 체크
        que = Queue(20000)
        visited = [[False] * c for _ in range(0, r)]
        visited[0][0] = True
        que.enqueue((0, 0))

        while not que.is_empty():
            row, col = que.dequeue()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if visited[next_row][next_col]:
                    continue
                # 0인부분만 탐색
                if arr[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                que.enqueue((next_row, next_col))
        # 0이면서, visited가 방문 안한 좌표가 치즈구멍
        for row in range(0, r):
            for col in range(0, c):
                if arr[row][col] == 0 and not visited[row][col]:
                    arr[row][col] = -1

        # 공기와 맞닿아있는 치즈 찾기
        cnt = 0
        for row in range(0, r):
            for col in range(0, c):
                if arr[row][col] == 1:
                    cnt += 1
                    flag = False
                    for d in range(0, 4):
                        next_row = row + dr[d]
                        next_col = col + dc[d]
                        if arr[next_row][next_col] == 0:
                            flag = True
                            break
                    if flag:
                        arr[row][col] = 2
        # 공기 닿은 치즈 제거 + 치즈 구멍 다시 0으로 초기화
        for row in range(0, r):
            for col in range(0, c):
                if arr[row][col] == 2 or arr[row][col] == -1:
                    arr[row][col] = 0
        
        # 치즈 남았는지 체크
        flag = False
        for row in range(0, r):
            if flag:
                break
            for col in range(0, c):
                if arr[row][col]:
                    flag = True
                    break
        if not flag:
            return (time, cnt)
        time += 1

R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(map(int, input().split()))


answer = req_time_cheese_clear(MAP)
req_time = answer[0]
last_pieces = answer[1]
print(req_time)
print(last_pieces)