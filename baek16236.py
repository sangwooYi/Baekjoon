import sys
sys.stdin = open("baek16236.txt")

"""
최대 크기가 20이므로
BFS // DFS 둘다 상관없을듯?

point는 먹을 수 있는 물고기가 최단거리에
여러마리가 존재한다면
=> 가장 열이 낮고, 같은 열중에서라도 가장 행이 낮은애를 탐색하는과정이 필요

문제 잘 읽자!!
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


def baby_shark(arr, n):
    que = Queue(n**3)
    visited = [[False] * n for _ in range(0, n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    flag = False
    for i in range(0, n):
        if flag:
            break
        for j in range(0, n):
            if arr[i][j] == 9:
                flag = True
                arr[i][j] = 0
                que.enqueue((i,j,0))
                visited[i][j] = True
                break
    size = 2
    # count == size가 될때 size += 1 그리고 count 초기화
    count = 0
    total_time = 0
    while True:
        temp = []
        while not que.is_empty():
            now = que.dequeue()
            row = now[0]
            col = now[1]
            path = now[2]
            for dir in range(0, 4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]
                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                    continue
                if visited[next_row][next_col]:
                    continue
                # 자기보다 덩치 큰애는 못지나감!
                if arr[next_row][next_col] > size:
                    continue
                visited[next_row][next_col] = True
                if arr[next_row][next_col] < size and arr[next_row][next_col] > 0: 
                    temp.append((next_row, next_col, path+1))
                    continue
                que.enqueue((next_row, next_col, path+1))
        # 최단거리가 중복되는경우 가장 가까운애, 최소 행, 그 중에서도 최소 열
        if temp:
            temp.sort(key=lambda x: (x[2], x[0], x[1]))
            # 먹는 처리
            arr[temp[0][0]][temp[0][1]] = 0
            count += 1
            # 만약 size만큼 먹었으면 size + 1 , 그리고 count 초기화
            if count == size:
                size += 1
                count = 0
            # 먹은 포인트에서부터 다시 시작
            que.enqueue((temp[0][0], temp[0][1], 0)) 
            visited = [[False] * n for _ in range(0, n)]
            visited[temp[0][0]][temp[0][1]] = True
            total_time += temp[0][2]
        # 더 먹을애 없으면 끝
        else:
            return total_time


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

ans = baby_shark(MAP, N)
print(ans)