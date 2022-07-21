import sys
sys.stdin = open("baek19238.txt")

"""
N은(맵 사이즈 2 <= N <= 20) 최대 20, M은(승객 수) 최대 400 (1 <= M <= N**2)
초기연료값은 최대 50만
맵에서 0은 빈칸, 1은 벽

태울때 우선순위는
최단거리 => 여러명이면 행 작은 승객 => 그래도 여러명이면 열이 작은 승객
태우고 목적지 까지도 최단거리이동
목적지 성공 시 => 출발 ~ 도착 거리까지 소모 연료의 2배만큼 충전

따라서 최대 M번만큼 반복
BFS 돌면서 
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



def calc_req(arr, clients, init_data):
    # 맵 size, 승객 수, 초기 연료, 백준의 위치
    size, client_num, fuel, baek_row, baek_col = init_data

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 승객 이송 완료 카운팅 
    cnt = 0
    while cnt < client_num:
        que = Queue(size*size*10)
        visited = [[False] * size for _ in range(0, size)]
        # 현재 백준 위치 입력
        que.enqueue((baek_row, baek_col, 0))
        visited[baek_row][baek_col] = True
        # 바로 태울 수 있는 경우 (현재 백준 위치와 겹친경우가 무조건 최단거리)
        if arr[baek_row][baek_col] == 2:
            start_row = baek_row
            start_col = baek_col      
        # 최단거리 승객을 찾아야 함
        else:
            temp = []
            while not que.is_empty():
                row, col, path = que.dequeue()
                for k in range(0, 4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]
                    next_path = path + 1
    
                    # 맵 밖
                    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                        continue
                    # 이미 방문
                    if visited[next_row][next_col]:
                        continue
                    # 벽
                    if arr[next_row][next_col] == 1:
                        continue
                    visited[next_row][next_col] = True
                    # 이동 가능한 경우 중 승객이 있는 경우
                    if arr[next_row][next_col] == 2:
                        # 경로, 승객 위치를 저장 
                        temp.append([next_path, next_row, next_col])
                    que.enqueue((next_row, next_col, next_path))
            if temp:
                # 최단거리 => 행 오름차순 => 열 오름차순 순으로 정렬
                temp.sort(key=lambda x : (x[0], x[1], x[2]))
                distance, start_row, start_col = temp[0]
                # 현재 남아있는 연료로 못가는 경우
                if distance > fuel:
                    return -1
                # 이동 가능하면 그만큼 연료 감소
                fuel -= distance
            # 태울 수 있는 사람이 없는 경우도 더 이상 진행 불가
            else:
                return -1
        end_row, end_col = clients[(start_row, start_col)]
        arr[start_row][start_col] = 0 
        # 찾고 나서 태운 승객을 목적지까지 이동 
        que = Queue(size*size)
        visited = [[False] * size for _ in range(0, size)]
        que.enqueue((start_row, start_col, 0))
        while not que.is_empty():
            row, col, path = que.dequeue()

            for k in range(0, 4):
                next_row = row + dr[k]
                next_col = col + dc[k]
                next_path = path+1
                # 이런 실수 조심하자..
                if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                    continue
                if visited[next_row][next_col]:
                    continue
                if arr[next_row][next_col] == 1:
                    continue
                # 목적지 도착 시 처리 후 종료
                visited[next_row][next_col] = True
                if next_row == end_row and next_col == end_col:
                    # 도착 못할 경우 바로 취소
                    if next_path > fuel:
                        return -1
                    # 도착 가능한 경우 fuel - next_path + 2*(next_path) 
                    fuel += next_path
                    cnt += 1
                    baek_row = end_row
                    baek_col = end_col
                    break
                que.enqueue((next_row, next_col, next_path))

    return fuel               

# 맵 사이즈, 승객 수, 초기 연료
N, M, F = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
# 백준이의 위치(행, 열은 1부터시작, 인덱스와 1차이)
R, C = map(int, input().split())
client_dict = {}
# 출발지 행, 열 / 도착지 행, 열 정보가 주어짐
for i in range(0, M):
    start_row, start_col, end_row, end_col = map(int, input().split())
    # 승객은 2로 (태우고나면 0으로 바꾸면 된다.)
    # 미리 인덱스와 싱크 맞추기
    MAP[start_row-1][start_col-1] = 2
    # (시작 행, 시작 열) 을 key 값으로, [도착 행, 도착 열]를 value 값으로
    client_dict[(start_row-1, start_col-1)] = [end_row-1, end_col-1]

answer = calc_req(MAP, client_dict, (N, M, F, R-1, C-1))
print(answer)