import sys
from collections import deque
sys.stdin = open("baek16954.txt")

"""
8*8 맵으로 고정,
따라서 시간적으로는 여유가 있다.

무조건 좌측아래에서 시작 (7,0) 목표는 우측상단 (0, 7)
근데 그냥 제위치에 있을 수도 있고, 방문한데를 또 방문해도 문제 없음!
=> 따라서 최단 경로는 애초에 구하기 힘들고, 문제 자체가 가능여부만 따지고 있음
그냥 벽돌 아무리많아도 8턴이면 다없어지는 것을 이용해서, 발상의 전환!
벽돌 다 사라질떄까지 살아남은 경우가 있으면 무조건 탈출 가능하다고 보는것!
=> 이걸로 해결
"""

def is_possible(arr):
    # 사이즈 8*8
    size = len(arr)
    block = "#"
    
    # 대각선으로도 이동 가능
    # 상 우상 우 우하 하 좌하 좌 좌상 제자리
    dr = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
    dc = [0, 1, 1, 1, 0, -1, -1, -1, 0]

    que = deque()
    que.append((size-1, 0))
    # 매턴
    while True:
        next_block_pos = {}
        flag = False
        for i in range(0, size):
            for j in range(0, size):
                if arr[i][j] == block:
                    flag = True
                    # size-1 행에있는 벽돌들은 어차피 다음턴에 사라짐
                    if i < size-1:
                        # 다음 턴 블록 위치를 미리 저장 (이쪽으로도 결국 못 가기 때문)
                        next_block_pos[(i+1, j)] = 1
        # 벽돌이 아예 없으면 무조건 탈출 가능
        if not flag:
            return 1
        # 현재 턴에 가능한 위치를 저장
        tmp_que = deque()

        while que:
            row, col = que.popleft()

            for d in range(0, len(dr)):
                next_row = row + dr[d]
                next_col = col + dc[d]
                
                if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                    continue
                # 현재 턴에 블록이 있는 곳
                if arr[next_row][next_col] == block:
                    continue
                # 다음턴에 블록 떨어질 위치
                if (next_row, next_col) in next_block_pos.keys():
                    continue
                tmp_que.append((next_row, next_col))
        # 다음턴 까지 살아남을 수 있는 위치가 없음
        if not tmp_que:
            return 0
        next_blocks = list(next_block_pos.keys())
        # 다음턴에 쓸수 있는 블록이 하나도 없으면 어차피 끝
        if len(next_block_pos) == 0:
            return 1
        # 다음 턴 용 arr 만들기   
        tmp_arr = [["."] * size for _ in range(0, size)]
        for i in range(0, len(next_blocks)):
            tmp_arr[next_blocks[i][0]][next_blocks[i][1]] = block
        arr = tmp_arr
        while tmp_que:
            row, col = tmp_que.popleft()
            que.append((row, col))

size = 8
MAP = [0] * size
for i in range(0, size):
    MAP[i] = list(input())

answer = is_possible(MAP)
print(answer)