import sys
sys.stdin = open("baek13460.txt")

"""
N, M 최소 3, 최대 10

# 벽, R은 빨간구슬 B는 파란구슬 O는 구멍 .는 빈칸

기울이는 방향은 4가지 (상하좌우)로 선택가능하며
한쪽방향으로 기울이면, 각 구슬은 더이상 동 못할때까지 굴러간다.

문제에서 기본적으로 #에 둘러쌓여있어, 맵 밖으로 벗어날 일은 없음

매번 depth에서 상,하,좌,우 모든방향을 진행
각 방향마다 새로운 결과에따라 새로운 리스트를 생성하여 
그 리스트를 인자로 전달
=> 이걸 반복해서 빨간구슬이 도달하는 경우만 체크
=> 그 중에서 최솟값 

최대 10x10이므로 매 재귀마다 R, B 위치 일일이 찾아도 크게 문제 없음

# 종료조건
1. 파란볼이 먼저 구멍에 도달하는 경우
2. 현재까지 체크된 최솟값보다 더 많은횟수를 진행하는 경우

매 반복마다 기존 파란공, 빨간공 위치 저장.
굴린 이후에 최종 위치 확인
=> 새로운 리스트는 우선 기존 리스트 그대로 깊은 복사 한 후에
기존 위치는 빈칸으로, 최종위치에는 R, B를 각각 대입

중요한건 굴러가는게 동시에 굴러간다는 것!
따라서 굴리는 방향마다, 만약 동선이 겹치는 경우가 있다면
더 가까운애를 찾는 작업이 필요!
(그럼 그 전에 벽에 막히던 말건 문제없이 진행 가능)

도중에 O를 만나도 종료조건이다! 이거 조심 ㅠㅠ
동시에 빠져도 실패다! + 10회 이하로 해결해야함

문제좀 잘 읽자 ㅡㅡ


일단 BFS로 풀고, DFS 풀이도 봐보자.
일단 최소 경로는 보통 BFS 쪽으로 가면 됨
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
    

def who_is_first(red, blue, direction):
    # 굴리는 방향마다 벽에 더 가까운애를 먼저 진행해야함
    if direction == 0:
        # 윗방향 굴릴떄, row 좌표가 작은애가 더 먼저
        # row 값이 같으면 col이 다른거니까 이떄는 어떤걸 먼저하던 상관 없다.
        if red[0] <= blue[0]:
            # first 값이 0이면 빨간볼을 먼저, 1이면 파란볼을 먼저하는걸로 설정
            first = 0
        else:
            first = 1
    elif direction == 1:
        # 아랫방향 굴릴때, row가 더 큰애를 먼저
        if red[0] >= blue[0]:
            first = 0
        else:
            first = 1
    elif direction == 2:
        # 왼쪽방향, col 값이 작은애가 먼저
        if red[1] <= blue[1]:
            first = 0
        else:
            first = 1
    elif direction== 3:
        # 오른방향, col 값이 큰애가 먼저
        if red[1] >= blue[1]:
            first = 0
        else:
            first = 1

    return first


def bfs(arr, r, c):

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
   
    que = Queue(100000)
    que.enqueue((arr, 1))

    while not que.is_empty():
        tmp = que.dequeue() 
        now = tmp[0]
        turn = tmp[1]
        
        for i in range(0, r):
            for j in range(0, c):
                if now[i][j] == "R":
                    red = (i, j)
                elif now[i][j] == "B":
                    blue = (i, j)
        for i in range(0, 4):
            order = who_is_first(red, blue, i)
            # 빨간공 먼저
            if order == 0:
                term = 1
                next_red_row = red[0] + (term*dr[i])
                next_red_col = red[1] + (term*dc[i])
                r_flag = False
                while 0 <= next_red_row < r and 0 <= next_red_col < c:
                    next_red_row = red[0] + (term*dr[i])
                    next_red_col = red[1] + (term*dc[i])

                    if now[next_red_row][next_red_col] == "#":
                        break
                    
                    # 도중에 구멍 만나도 종료
                    if now[next_red_row][next_red_col] == "O":
                        r_flag = True
                        break
                    term += 1
                # 구멍 만난 경우는 next_red_row, next_red_col 그대로 유지
                if not r_flag:
                    next_red_row = red[0] + ((term-1)*dr[i])
                    next_red_col = red[1] + ((term-1)*dc[i])
     
                term = 1
                next_blue_row = blue[0] + (term*dr[i])
                next_blue_col = blue[1] + (term*dc[i])
                b_flag = False
                while 0 <= next_blue_row < r and 0 <= next_blue_col < c:
                    next_blue_row = blue[0] + (term*dr[i])
                    next_blue_col = blue[1] + (term*dc[i])

                    if now[next_blue_row][next_blue_col] == "#":
                        break
                    if arr[next_blue_row][next_blue_col] == "O":
                        b_flag = True
                        break
                    if next_blue_row == next_red_row and next_blue_col == next_red_col:
                        break
                    term += 1
                if not b_flag:
                    next_blue_row = blue[0] + ((term-1)*dr[i])
                    next_blue_col = blue[1] + ((term-1)*dc[i])  
                # 만약 b가 구멍에 빠지면 진행하면 안됨
        
                if r_flag:
                    if b_flag:
                        continue
                    return turn

            # 파란공 먼저
            elif order == 1:
                term = 1
                next_blue_row = blue[0] + (term*dr[i])
                next_blue_col = blue[1] + (term*dc[i])
                b_flag = False
                while 0 <= next_blue_row < r and 0 <= next_blue_col < c:
                    next_blue_row = blue[0] + (term*dr[i])
                    next_blue_col = blue[1] + (term*dc[i])

                    if now[next_blue_row][next_blue_col] == "#":
                        break
                    
                    if now[next_blue_row][next_blue_col] == "O":
                        b_flag = True
                        break
                    term += 1
                # 진행하면 안됨
                if b_flag:
                    continue
                next_blue_row = blue[0] + ((term-1)*dr[i])
                next_blue_col = blue[1] + ((term-1)*dc[i])  
                # 진행되면 안되는 방향   
                if now[next_blue_row][next_blue_col] == "O":
                    continue
                term = 1
                next_red_row = red[0] + (term*dr[i])
                next_red_col = red[1] + (term*dc[i])
                r_flag = False
                while 0 <= next_red_row < r and 0 <= next_red_col < c:
                    next_red_row = red[0] + (term*dr[i])
                    next_red_col = red[1] + (term*dc[i])

                    if now[next_red_row][next_red_col] == "#":
                        break
                    if next_red_row == next_blue_row and next_red_col == next_blue_col:
                        break
                    # 도중에 구멍 만나도 종료
                    if now[next_red_row][next_red_col] == "O":
                        r_flag = True
                        break              
                    term += 1
                if r_flag:
                    return turn
                next_red_row = red[0] + ((term-1)*dr[i])
                next_red_col = red[1] + ((term-1)*dc[i])
                if now[next_red_row][next_red_col] == "O":
                    return turn
            # 값이 변했을 경우만
            if red[0] == next_red_row and red[1] == next_red_col and blue[0] == next_blue_row and blue[1] == next_blue_col:
                continue
            # 11회 째라면 중단시켜야 함
            if turn > 10:
                return -1
            temp = [[0] * c for _ in range(0, r)]
            for row in range(0, r):
                for col in range(0, c):
                    temp[row][col] = now[row][col]
            temp[red[0]][red[1]] = "."
            temp[blue[0]][blue[1]] = "."
            temp[next_red_row][next_red_col] = "R"
            temp[next_blue_row][next_blue_col] = "B"
            que.enqueue((temp, turn+1))
    return -1

# row 가 N col이 M
N, M = map(int, input().split())
MAP = [[0] * M for _ in range(0, N)]
for i in range(0, N):
    MAP[i] = list(input())


answer = bfs(MAP, N, M)
print(answer)