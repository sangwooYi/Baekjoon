import sys
sys.stdin = open("baek2667.txt")

"""
문제 잘 읽자!
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

# 최대 25니까 완전탐색 충분히 가능
def find_complex(arr, n):
    que = Queue(n*n)
    visited = [[False] * n for _ in range(0, n)]
    
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    comp_count = 0
    counting = []
    for row in range(0, n):
        for col in range(0, n):
            if arr[row][col] == 0:
                continue
            if visited[row][col]:
                continue
            comp_count += 1
            que.enqueue((row, col))
            visited[row][col] = True
            count = 1
            while not que.isEmpty():
                now = que.dequeue()
                for dir in range(0, 4):
                    next_row = now[0] + dr[dir]
                    next_col = now[1] + dc[dir]
                    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if arr[next_row][next_col] == 0:
                        continue
                    count += 1
                    visited[next_row][next_col] = True
                    que.enqueue((next_row, next_col))
            counting.append(count)
    counting.sort()
    res = [comp_count]
    for i in range(0, len(counting)):
        res.append(counting[i])
    return res

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))

ans = find_complex(MAP, N)
for i in range(0, len(ans)):
    print(ans[i])