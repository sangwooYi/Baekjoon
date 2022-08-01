import sys
sys.stdin = open("baek20058.txt")

"""
문제 이해를 똑바로 하자!

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


def calc_area(arr, size):
    visited = [[False] * size for _ in range(0, size)]
    que = Queue(size*size*10)

    max_area = 0
    while True:
        flag = True
        start_row = 0
        start_col = 0
        for i in range(0, size):
            if not flag:
                break
            for j in range(0, size):
                if not visited[i][j]:
                    flag = False
                    visited[i][j] = True
                    start_row = i
                    start_col = j
                    break
        if flag:
            return max_area
        if arr[start_row][start_col]:
            que.enqueue((start_row, start_col))
            tmp_area = 1
            while not que.is_empty():
                row, col = que.dequeue()

                for k in range(0, 4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]

                    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if arr[next_row][next_col] == 0:
                        continue
                    visited[next_row][next_col] = True
                    tmp_area += 1
                    que.enqueue((next_row, next_col))
            max_area = max(max_area, tmp_area)

"""
part1  part2

part3  part4

각 격자가 90도 회전되어 이동하는것이다!
"""
def tornado(arr, n, size):
    # 격자 회전
    term = 2**n
    if n > 0:
        temp = [[0] * size for _ in range(0, size)]

        # size는 인덱스 범위가 아니므로 자동으로 실행 안됨
        for row in range(0, size, term):
            for col in range(0, size, term):
                for i in range(0, term):
                    for j in range(0, term):
                        # j번쨰 열은 j번쨰 행으로, i번째 행은 term-i번째 열이 되는것
                        temp[row+j][col+term-1-i] = arr[row+i][col+j]

        arr = temp
 
    temp = [[0] * size for _ in range(0, size)]
    # 회전후 얼음 인접칸 3칸이상 없으면 1 감소
    for row in range(0, size):
        for col in range(0, size):
            # 아직 값이 있는 경우만 진행
            if arr[row][col]:
                cnt = 0
                for k in range(0, 4):
                    next_row = row + dr[k]
                    next_col = col + dc[k] 
                    
                    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                        continue
                    if arr[next_row][next_col]:
                        cnt += 1
                # 줄어들어야 할 칸 표기
                if cnt < 3:
                    temp[row][col] = 1
    
    for row in range(0, size):
        for col in range(0, size):
            if temp[row][col]:
                arr[row][col] -= 1
    
    return arr


N, Q = map(int, input().split())
size = 2**N
A = [0] * size
for i in range(0, size):
    A[i] = list(map(int, input().split()))
steps = list(map(int, input().split()))

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

total = 0
area = 0

new_arr = A


for step in steps:
    new_arr = tornado(new_arr, step, size)

for r in range(0, size):
    for c in range(0, size):
        total += new_arr[r][c]

area = calc_area(new_arr, size)

print(total)
print(area)