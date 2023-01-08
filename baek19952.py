import sys
sys.stdin = open("baek19952.txt")
from collections import deque

"""
항상 BFS를 풀때,
방문지점을 재방문하는 문제인지 체크!
+ 문제를 잘 읽자!
현재 힘보다 높은 높이차면 이동을 못하는것 뿐이지,
이동할때 그만큼 힘을 소모하는게 아님!
따라서 그냥 최단경로로 이동하면 됨! (즉 한번 방문한곳은 방문 안하는게 가장 이득)
"""

def is_possible():
    
    visited = [[False] * W for _ in range(0, H)]
    
    que = deque()
    start_row = Xs-1
    start_col = Ys-1
    end_row = Xe-1
    end_col = Ye-1
    
    visited[start_row][start_col] = True
    que.append((start_row, start_col, F, MAP[start_row][start_col]))

    while que:
        row, col, strength, height = que.popleft()

        if strength <= 0:
            continue

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            
            if visited[next_row][next_col]:
                continue
            next_height = MAP[next_row][next_col]
            if next_row == end_row and next_col == end_col:
                return "잘했어!!"
            if next_height > height:
                req_strength = next_height-height
                if req_strength > strength:
                    continue
            next_strength = strength-1
            visited[next_row][next_col] = True
            que.append((next_row, next_col, next_strength, next_height))   
    return "인성 문제있어??"

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(0, T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())
    
    MAP = [[0] * W for _ in range(0, H)]
    for i in range(0, O):
        x, y, l = map(int, input().split())
        MAP[x-1][y-1] = l
    answer = is_possible()
    print(answer)