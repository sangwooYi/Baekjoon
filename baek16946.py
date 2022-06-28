import sys
from collections import deque
sys.stdin = open("baek16946.txt")

"""
기본적인 풀이
=> 모든 벽에 대해 탐색
=> 그 벽을 0으로 바꾼뒤 BFS 진행, 이동 칸수를 result 배열에 해당 벽 칸 위치에 저장
=> 모든 벽에 대해 이 작업을 행한 뒤, 결과를 return

최악의 경우는 
벽이 50만개정도 있는 경우?
=> 50만 * 50만 ...?? 
(시간 초과!)

최적화를 해보자!
=> 뭔가 한번 탐색에서 전부다 체크하는 방법을 고민해봐야할듯?
=> 역발상!!
1. 빈칸에 대해서만 BFS 진행, 오히려 빈칸에다가 이동 가능한 칸수를 저장
2. 그다음 순회하면서 1이 나오면, (4방향에 있는 값 + 본인칸) % 10 을 1칸에다가 저장하면 됨!
( 결국 같은 로직인것!!! ) 이런생각을 혼자 할 수 있어야 한다
근데 여기서 4방향에 있는 값중 이어져 있는 값이 있을 수 있다.
따라서 같은 영역에 있는건지 표기할 값이 필요함!

시간초과...

=> 이걸 한번 반복에 전부 해결할 수 있게 코드를 짜야 한다.

그리고 deque가 내가 짠 Queue보다 빠르다 ... ㅠㅠ
.append() 가 enqueue()
.popleft() 가 dequeue() 다. 쓰는건 편함
"""


def baek_16946(arr, r, c):
    # 결과 반환용 리스트
    result = [[0] * c for _ in range(0, r)]


    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 초기화
    for i in range(0, r):
        for j in range(0, c):
            if arr[i][j]:
                result[i][j] = 1

    visited = [[False] * c for _ in range(0, r)]
    for i in range(0, r):
        for j in range(0, c):
            # 빈칸 + 아직 방문 안한경우에만 시작
            if arr[i][j] == 0 and not visited[i][j]:
                que = deque()
                # 방문위치 저장용
                que.append((i, j))
                visited[i][j] = True
                count = 1

                # 1인 좌표를 저장
                tmp = []
                          
                while que:
                    row, col = que.popleft()
                    
                    for k in range(0, 4):
                        next_row = row + dr[k]
                        next_col = col + dc[k]

                        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                            continue
                        if visited[next_row][next_col]:
                            continue
                        visited[next_row][next_col] = True
                        if arr[next_row][next_col] == 0:
                            count += 1
                            que.append((next_row, next_col))
                        else:
                            tmp.append((next_row, next_col))
                
                for k in range(0, len(tmp)):
                    row, col = tmp[k]
                    visited[row][col] = False
                    result[row][col] += count
                    if result[row][col] >= 10:
                        result[row][col] %= 10

    return result
                




# row, col
N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().strip()))


answer = baek_16946(MAP, N, M)

for i in range(0, N):
    print(''.join(map(str, answer[i])))