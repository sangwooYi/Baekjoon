import sys
sys.stdin = open("baek14502.txt")
"""
0은 빈칸, 1은 벽 2는 바이러스

풀이Idea.
빈칸 좌표를 전부 체크한뒤에
빈칸C3 만큼 조합을 돌린다. 각 경우에 맞게 전부
MAP을 새로 만들어서 => BFS를 돌림,
BFS 돌린 이후에 0의 갯수를 세어서
가장 0이 많은 애를 답으로!

이게 되네ㅡㅡ?
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


def virus(arr, cases):
    que = Queue(3000)

    n = len(arr)
    m = len(arr[0])
    box = [0] * n

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(0, n)]
    # 복사
    flag = False
    for row in range(0, n):
        temp = [0] * len(arr[0])
        for col in range(0, m):
            temp[col] = arr[row][col]
            if arr[row][col] == 2 and not flag:
                # 미리 세팅
                que.enqueue((row, col))
                visited[row][col] = True
                flag = True
        box[row] = temp
    for i in range(0, len(cases)):
        r, c = cases[i]
        box[r][c] = 1
    
    while True:
        while not que.is_empty():
            row, col = que.dequeue()

            for dir in range(0, 4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]
                if next_row < 0 or next_col < 0 or next_row >= n or next_col>= m:
                    continue
                if visited[next_row][next_col]:
                    continue
                # 1, 2  둘다 제외
                if box[next_row][next_col]:
                    continue
                # 방문처리하고, 바이러스 처리
                visited[next_row][next_col] = True
                box[next_row][next_col] = 2
                que.enqueue((next_row, next_col))
        flag = True
        for i in range(0, n):
            if not flag:
                break
            for j in range(0, m):
                # 바이러스중에서 아직 방문 안한애 있으면 체크
                if box[i][j] == 2 and not visited[i][j]:
                    que.enqueue((i, j))
                    visited[i][j] = True
                    flag = False
                    break
        if flag:
            break
    result = 0
    for i in range(0, n):
        for j in range(0, m):
            if box[i][j] == 0:
                result += 1
    return result

def comb(arr, start, visited, n, r):
    global answer 
    if r == 0:
        temp = [0] * 3
        idx = 0
        for i in range(0, len(arr)):
            if visited[i]:
                temp[idx] = arr[i]
                idx += 1
        now = virus(MAP, temp)
        if now >= answer:
            answer = now
        return
    for i in range(start, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, i+1, visited, n, r-1)
        visited[i] = False


# N*M 크기
N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

coords = []
for row in range(0, N):
    for col in range(0, M):
        if MAP[row][col] == 0:
            coords.append((row, col))
check = [False] * len(coords)

answer = 0
comb(coords, 0, check, len(coords), 3)
print(answer)