import sys
sys.stdin = open("baek2638.txt")

"""
녹는 치즈 조건
4변중 2변 이상이 외부와 접촉
=> 외부와 접촉은
=> 마주보는 변이 0이고, 치즈에 둘러쌓이지 않은 경우
치즈 내부공간 체크 idea,
가장 바깥자리는 무조건 0이므로, 여기서부터 BFS 시작
=> 처리되지 않은 공간은 내부공간인것! 
시간초과 안나네 ㅠㅠ
"""
class Queue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.front = 0
        self.rear = 0
        self.data = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear == 0
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



def cheese(arr, r, c):
          # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0
    while True:
        visited = [[False] * c for _ in range(0, r)]
        visited[0][0] = True
        que = Queue(10000)
        que.enqueue((0, 0))
        while not que.is_empty():
            row, col = que.dequeue()
            for dir in range(0, 4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if visited[next_row][next_col]:
                    continue
                if arr[next_row][next_col] == 1:
                    continue
                visited[next_row][next_col] = True
                que.enqueue((next_row, next_col))
        t_q = Queue(1000)
        for row in range(0, r):
            for col in range(0, c):
                # 치즈일때만
                if arr[row][col] == 1:
                    count = 0
                    for dir in range(0, 4):
                        n_row = row + dr[dir]
                        n_col = col + dc[dir]
                        if n_row < 0 or n_col < 0 or n_row >= r or n_col >= c:
                            continue
                        if arr[n_row][n_col] == 0 and visited[n_row][n_col]:
                            count += 1
                    if count >= 2:
                        t_q.enqueue((row, col))
        while not t_q.is_empty():
            now = t_q.dequeue()
            arr[now[0]][now[1]] = 0
        
        flag = True
        for row in range(0, r):
            if not flag:
                break
            for col in range(0, c):
                if arr[row][col]:
                    flag = False
                    break
        if flag:
            return result + 1
        else:
            result += 1


N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
ans = cheese(MAP, N, M)
print(ans)