import sys
sys.stdin = open("baek17836.txt")
"""
애초에 갈길이 없거나,
시간안에 못가는 경우 둘다 Fail

그냥 아래와같이 병렬적인 진행을 해야할때
저번처럼 3차원 리스트 선언하지말고,
그냥 별도의 visited 리스트를 사용하자 (난 이게 더 쉽다.)
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


def recue(arr, r, c, t):
    que = Queue(10000)
    # 3차원 리스트 선언 [그람 획득여부][행][열]
    visited = [[False] * c for _ in range(0, r)]
    gram_visited = [[False] * c for _ in range(0, r)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que.enqueue((0, 0, 0, False))
    visited[0][0] = True

    while not que.is_empty():
        row, col, path, is_gram = que.dequeue()
        if path > t:
            return "Fail"
        if row == r-1 and col == c-1:
            return path

        for dir in range(0, 4):
            next_row = row + dr[dir]
            next_col = col + dc[dir]

            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            if is_gram:
                if gram_visited[next_row][next_col]:
                    continue
                gram_visited[next_row][next_col] = True
                que.enqueue((next_row, next_col, path+1, is_gram))
            else:
                if visited[next_row][next_col]:
                    continue
                if arr[next_row][next_col] == 1:
                    continue
                if arr[next_row][next_col] == 2:
                    gram_visited[next_row][next_col] = True
                    que.enqueue((next_row, next_col, path+1, True))
                visited[next_row][next_col] = True
                que.enqueue((next_row, next_col, path+1, False))

    return "Fail"

N, M, T = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
ans = recue(MAP, N, M, T)
print(ans)