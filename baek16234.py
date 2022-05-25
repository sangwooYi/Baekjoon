import sys
sys.stdin = open("baek16234.txt")

"""
매 반복마다

영역간 인구수 차 비교,
L <= 인구수차 <= R 일때만 국경 open
BFS 이용하여 국경 오픈 가능한 영역들 체크,

visited 기본적으론 0
=> 연속된 연합국 갯수를 여기에 저장?

연합된 영역에 대해서는 
인구수 합 // 연합 칸수 로 인구수 갱신


다시 처음부터 진행

=> 아무데도 없으면 위 과정 반복 횟수를 반환 (이게 답)
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



def how_many_loop(arr, l, r):
    size = len(arr)
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    count = 0
    while True:
        # 매번 반복 진행
        visited = [[False] * size for _ in range(0, size)]
        que = Queue(size*size*10)

        flag = False
        for i in range(0, size):
            for j in range(0, size):
                # 이미 방문처리 된건 pass
                if visited[i][j]:
                    continue
                # 방문 처리
                visited[i][j] = True
                # 시작 위치
                que.enqueue((i, j))
                # 연결된 연합국 저장
                temp = [[i, j]]
                # 연속 칸수 체크
                straight = 1
                while not que.is_empty():
                    now = que.dequeue()
                    row = now[0]
                    col = now[1]
                    # 현재 칸 인구수
                    cur_p = arr[row][col]
                    for k in range(0, 4):
                        next_row = row + dr[k]
                        next_col = col + dc[k]

                        # 맵 밖인 경우
                        if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                            continue
                        # 이미 방문
                        if visited[next_row][next_col]:
                            continue
                        next_p = arr[next_row][next_col]
                        # 인구수 차
                        delta_p = abs(cur_p - next_p)
                        # 인구수 차이가 조건 안에 들어올 경우만
                        if delta_p < l or delta_p > r:
                            continue
                        visited[next_row][next_col] = True
                        # 한번이라도 연합국 발생
                        flag = True
                        straight += 1
                        temp.append([next_row, next_col])
                        que.enqueue((next_row, next_col))

                total = 0
                for k in range(0, len(temp)):
                    a, b = temp[k]
                    total += arr[a][b]
                conv_to = total // straight
                
                for k in range(0, len(temp)):
                    a, b = temp[k]
                    arr[a][b] = conv_to

        # 연합국 발생 X
        if not flag:
            return count
        # 연합국 발생된 경우 다음 반복
        count += 1

# 땅 크기, L <= 인구수차 <= R 일때만 국경 open
N, L, R = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

answer = how_many_loop(MAP, L, R)
print(answer)