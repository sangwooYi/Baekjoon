import sys

sys.stdin = open("baek1012.txt")

"""
BFS 사용!
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
        if self.rear == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


def find_min_require(maps, visited, r, c, start):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = Queue(r*c)
    # 초깃값 세팅
    que.enqueue(start)
    visited[start[0]][start[1]] = True
    ans = 1
    while True:
    # 이 while 문이 돌고 나면 인접한 모든 애들은 체크 된것
        while not que.is_empty():
            now = que.dequeue()
            row = now[0]
            col = now[1]
            for dir in range(0, 4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]

                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if visited[next_row][next_col]:
                    continue
                if maps[next_row][next_col] == 0:
                    continue
                visited[next_row][next_col] = True
                que.enqueue((next_row, next_col))
        flag = False
        for row in range(0, r):
            if flag:
                break
            for col in range(0, c):
                # 아직 방문안한데 있으면 체크해서 진행
                if not visited[row][col]:
                    next = (row, col)
                    flag = True
                    break
        if flag:
            ans += 1
            visited[next[0]][next[1]] = True
            que.enqueue(next)
        # 전부 방문했으면 ans 값 return
        else:
            return ans
        

T = int(input())
for tc in range(1, T+1):
    # 문제 잘 읽자!
    C, R, K = map(int, input().split())
    checked = [[True] * C for _ in range(0, R)]
    MAP = [[0] * C for _ in range(0, R)]
    for i in range(0, K):
        c, r = (map(int, input().split()))
        MAP[r][c] = 1
        checked[r][c] = False
    flag = False
    for row in range(0, R):
        if flag:
            break
        for col in range(0, C):
            if MAP[row][col] == 1:
                start = (row, col)
                flag = True
                break

    answer = find_min_require(MAP, checked, R, C, start)
    print(answer)