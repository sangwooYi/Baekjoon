import sys
sys.stdin = open("baek11559.txt")


"""
4개 이상 인접 (상/하/좌/우)해 있으면 터짐.
이런 그룹이 여러개라도 동시에 터지며 연쇄 횟수는 +1

따라서 
매 반복마다
현재 터질수 있는 그룹 전부 체크

=> 한 그룹도 없으면 or 아예 블록이 없으면 반복 종료
=> 터진 그룹이 있으면, 각 열마다 남은 블록 있는지 체크해서 바닥에 배치해준 후 
   다음 반복으로 진행

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




def puyo_puyo(arr):
    
    # 델타 함수는 아래 방법 둘다 상관 X 취향, 문제 성격에 따른 선택
    # [[-1, 0], [1, 0], [0, -1], [0, 1]] vs [-1, 1, 0, 0] / [0, 0, -1, 1]
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    R = 12
    C = 6
    hole = "."
    res = 0
    # 끝날때까지 반복 진행
    while True:
        # 터지는 그룹이 있는지 체크 flag
        game_flag = False
        visited = [[False] * C for _ in range(0, R)]
        
        while True:
            flag = False
            # 행은 맨 아래에서부터 역으로 진행하는게 효율적
            # 아직 체크할 블록이 있는지 체크
            for i in range(R-1, -1, -1):
                if flag:
                    break
                for j in range(0, C):
                    if not visited[i][j] and arr[i][j] != hole:
                        flag = True
                        start_row = i
                        start_col = j
                        block = arr[i][j] 
                        break                   
            # 모두 체크했으면 끝
            if not flag:
                break
            # print(arr)
            # 아직 남았으면 bfs 진행
            que = Queue(20000)
            que.enqueue((start_row, start_col))
            visited[start_row][start_col] = True
            # 터지는 블록 갯수 
            cnt = 1
            # 터뜨릴 애들 위치 저장
            boom_pos = [(start_row, start_col)]
            while not que.is_empty():
                row, col = que.dequeue()
                for d in range(0, 4):
                    next_row = row + dr[d]
                    next_col = col + dc[d]
                    # 맵 밖
                    if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                        continue
                    # 이미 방문
                    if visited[next_row][next_col]:
                        continue
                    # 빈 공간
                    if arr[next_row][next_col] == hole:
                        continue
                    # 다른 블록
                    if arr[next_row][next_col] != block:
                        continue
                    visited[next_row][next_col] = True
                    cnt += 1
                    que.enqueue((next_row, next_col))
                    boom_pos.append((next_row, next_col))

            # 4개 이상이면 터뜨림
            if cnt >= 4:
                game_flag = True
                for boom in boom_pos:
                    y, x = boom
                    # 빈공간으로 대체
                    arr[y][x] = hole

        # 터진 그룹이 없으면 종료
        if not game_flag:    
            break
        # 있으면 다음 게임을 위해 재배치
        temp = [[hole] * C for _ in range(0, R)]
        for j in range(0, C):
            tmp = []
            for i in range(R-1, -1, -1):
                if arr[i][j] != hole:
                    tmp.append(arr[i][j])
            
            if tmp:
                n = len(tmp)
                for k in range(0, n):
                    temp[R-1-k][j] = tmp[k]
        arr = temp
        res += 1
    return res



# 12행 6열로 필드가 고정
FIELD = [0] * 12
for i in range(0, 12):
    FIELD[i] = list(input())


answer = puyo_puyo(FIELD)
print(answer)