import sys
from collections import deque
sys.stdin = open("baek2573.txt")

"""
N, M 300 이하 (<= 90000)
아니 한번에 하는건 난 왜 안되는건데 ㅡㅡ?
"""

def count_area(arr):
    area = 0
    visited = [[False] * N for _ in range(0, M)]
    
    while True:
        flag = False

        for i in range(0, M):
            if flag:
                break
            for j in range(0, N):
                if arr[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                area += 1
                start_row = i
                start_col = j   
                visited[start_row][start_col] = True
                flag = True
                break
        que = deque()
        que.append((start_row, start_col))
        while que:
            row, col = que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= M or next_col >= N:
                    continue
                if arr[next_row][next_col] == 0:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                que.append((next_row, next_col))
        
        if not flag:
            return area

M, N = map(int, input().split())
MAP = [0] * M
for i in range(0, M):
    MAP[i] = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

req_year = 0
answer = 0
arr = MAP
while True:
    flag = False
    # 처음부터 두 덩이 or 다 녹아있는 상태일수 있으니, 체크부터 하고 진행
    for r in range(0, M):
        if flag:
            break
        for c in range(0, N):
            # 값이 있는애만 진행
            if arr[r][c]:
                flag = True
                break
    # 다 녹아 있음
    if not flag: 
        break
    area = count_area(arr)
    # 두덩이 이상 분리되어 있음
    if area > 1:
        answer = req_year
        break
    # 다음해로 진행
    req_year += 1
    temp = [[0] * N for _ in range(0, M)]
    for r in range(0, M):
        for c in range(0, N):
            if arr[r][c]:
                cnt = 0
                for d in range(0, 4):
                    next_r = r + dr[d]
                    next_c = c + dc[d]
                    if next_r < 0 or next_c < 0 or next_r >= M or next_c >= N:
                        continue
                    if arr[next_r][next_c] == 0:
                        cnt += 1
                next_val = arr[r][c] - cnt
                if next_val < 0:
                    next_val = 0
                temp[r][c] = next_val
    arr = temp
                
print(answer)
