import sys
sys.stdin = open("baek1941.txt")


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
        self.rear += 1
        self.data += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.front += 1
        self.data -= 1
        if self.front == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


def bfs(arr):

    check = [False] * len(arr)
    tmp_dict = {}
    for i in range(0, len(arr)):
        tmp_dict[arr[i]] = i
    check[0] = True
    que = Queue(100)
    que.enqueue(arr[0])

    while not que.is_empty():
        row, col = que.dequeue()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= 5 or next_col >= 5:
                continue
            if (next_row, next_col) not in tmp_dict.keys():
                continue
            idx = tmp_dict[(next_row, next_col)]
            if check[idx]:
                continue
            check[idx] = True
            que.enqueue((next_row, next_col))

    for i in range(0, len(check)):
        if not check[i]:
            return False
    return True



def comb(arr, fields, visited, start, n, r):
    global answer

    if r == 0:
        
        tmp = [0] * 7
        idx = 0
        S_cnt = 0
        for i in range(0, n):
            if visited[i]:
                row, col = arr[i]
                if fields[row][col] == "S":
                    S_cnt += 1
                tmp[idx] = (row, col)
                idx += 1
        if S_cnt < 4:
            return
        if bfs(tmp):
            answer += 1
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, fields, visited, i+1, n, r-1)
        visited[i] = False

MAP = [0] * 5
for i in range(0, 5):
    MAP[i] = list(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [False] * 25
arr = [0] * 25
idx = 0
for i in range(0, 5):
    for j in range(0, 5):
        arr[idx] = (i, j)
        idx += 1

answer = 0
comb(arr, MAP, visited, 0, 25, 7)
print(answer)