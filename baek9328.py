import sys
sys.stdin = open("baek9328.txt")

"""
ord(문자) => 유니코드로 반환
chr(유니코드) => 해당 유니코드의 문자로 반환

참고 a ~ z 는 97 ~ 122
     A ~ Z 는 65 ~ 90
따라서 소문자 -> 대문자는 (소문자 유니코드 - 32)
반대의 경우는 대문자 -> 소문자 는 (대문자 유니코드 + 32)

훔쳐야 하는 문서는 $
빈 공간은 .,  *는 벽 (이동 못함)
대문자는 문, 소문자는 열쇠, 대문자-소문자 매칭되는 모든 문을 열 수 있다.
상,하,좌,우로 이동 가능

BFS 
전략 1.
매 탐색마다 입장 가능한 포인트 체크.
(누적 개념으로 진행되야함)

각 포인트에서 열쇠를 얻거나 or 문서를 얻으면 유효함
아무런 변화가 없으면 종료 
이걸 계속 반복!

종료 조건
1. 모든 문서를 다 찾았을 경우
2. 이미 모든곳을 탐색해 보았을 경우
3. 문서 or 열쇠 획득 이벤트를 단 한번도 진행하지 못했을 경우

풀긴 풀었는데, 내 풀이 엄청 비효율적임 (시간, 공간복잡도 두 방향 모두다)
=> 쓸데없는 중복 진행이 많고, 딕셔너리를 너무 과하게 사용했다(딕셔너리는 메모리를 많이 먹는다)
다른 분들 코드 참고하고 공부할 것
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
        


def find_max(arr, h, w, keys, convert, upper_check):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 해당 키를 갖고있는거 바로 체크하기 위함, 대문자값을 key로 저장
    key_check = {}
    for i in range(0, len(keys)):
        upper_case = convert[keys[i]]
        key_check[upper_case] = 1
    
    # 문서 카운트
    count = 0
    total = 0
    # 문서 중복 획득 방지용
    doc_check = {}
    
    entry_point = []
    entry_check = {}
    # 가장자리에 열쇠가 있는지 체크 (얘는 한번만 하면되니까 여기에다가)
    # 가장자리에 문서가 있을수도 있다!
    for row in range(0, h):
        for col in range(0, w):
            # 총 문서 갯수 체크
            if arr[row][col] == "$":
                total += 1
            # 가장자리인 경우
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                if arr[row][col] == "$":
                    count += 1
                    doc_check[(row, col)] = 1          
                    entry_point.append((row, col))
                    entry_check[(row, col)] = 1
                if arr[row][col] == ".":
                    entry_check[(row, col)] = 1
                    entry_point.append((row, col))
                if arr[row][col] in convert.keys():
                    entry_check[(row, col)] = 1
                    entry_point.append((row, col))
                    key_check[convert[arr[row][col]]] = 1

    while True:
        # 매 반복마다 입장가능한 가장자리 체크 (최대 400회니까 일단 누적하지 말아보자)
        flag = False
        
        # 입장 가능한 가장자리 체크
        # 해당 값이 . 거나, 열쇠를 갖고있는 문일 경우 해당 위치 저장
        for i in range(0, w):
            if arr[0][i] in key_check.keys():
                if (0, i) not in entry_check.keys():
                    entry_check[(0, i)] = 1
                    entry_point.append((0, i))
            if arr[h-1][i] in key_check.keys():
                if (h-1, i) not in entry_check.keys():
                    entry_check[(h-1, i)] = 1
                    entry_point.append((h-1, i))
        for i in range(0, h):
            if arr[i][0] in key_check.keys():
                if (i, 0) not in entry_check.keys():
                    entry_check[(i, 0)] = 1
                    entry_point.append((i, 0))
            if arr[i][w-1] in key_check.keys():
                if (i, w-1) not in entry_check.keys():
                    entry_check[(i, w-1)] = 1
                    entry_point.append((i, w-1))
        
        # 들어갈수있는 곳 없으면 바로 끝
        if len(entry_point) == 0:
            return count

        # 출입 가능한 모든점을 각각 체크
        for i in range(0, len(entry_point)):
            r, c = entry_point[i]
            visited = [[False] * w for _ in range(0, h)]
            visited[r][c] = True
            
            que = Queue(h*w*10)
            que.enqueue((r, c))

            while not que.is_empty():
                row, col = que.dequeue()
                for k in range(0, 4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]
          
                    # 맵 밖 pass
                    if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w:
                        continue
                    # 벽 pass
                    if arr[next_row][next_col] == "*":
                        continue
                    # 열쇠 없는 문 pass (들다 참이어야 pass 하는 것)
                    if arr[next_row][next_col] in upper_check.keys() and not arr[next_row][next_col] in key_check.keys():
                        continue
                    # 이미 방문 pass
                    if visited[next_row][next_col]:
                        continue
                    # 이동 가능한곳
                    # 열쇠일 경우 획득 열쇠 추가, 아직 획득 안한경우만 추가
                    if arr[next_row][next_col] in convert.keys():
                        upper_case = convert[arr[next_row][next_col]]
                        if not upper_case in key_check.keys():
                            flag = True
                            key_check[upper_case] = 1

                    if arr[next_row][next_col] == "$":
                        # 현재 doc_check에 저장 안된 경우만 카운팅
                        if (next_row, next_col) not in doc_check.keys():
                            flag = True
                            count += 1
                            doc_check[(next_row, next_col)] = 1
                    visited[next_row][next_col] = True
                    que.enqueue((next_row, next_col))
            f = False
            for y in range(0, h):
                if f:
                    break
                for x in range(0, w):
                    if not visited[y][x]:
                        f = True
                        break
            if not f:
                return count
 
        # 문서 획득 or 열쇠 획득중 아무것도 안일어났으면 종료 (더이상 할게 없는것)
        if not flag:
            return count

# 해당 키(소문자)가 어떤 문(대문자)과 매칭인지 미리 선언
# 추가적으로 내가 이동한 위치에 열쇠가 있는지 체크도 가능
conv_to_upper = {}

# 대문자인지 체크용
upper_check = {}
for i in range(97, 123):
    upper = i-32
    lower = i
    conv_to_upper[chr(lower)] = chr(upper)
    upper_check[chr(upper)] = 1



T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    MAP = [0] * H
    for i in range(0, H):
        MAP[i] = list(input())
    keys = list(input())
    # 열쇠가 없는 경우
    if keys[0] == "0":
        keys = []

    answer = find_max(MAP, H, W, keys, conv_to_upper, upper_check)
    print(answer)