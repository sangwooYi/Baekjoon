import sys
sys.stdin = open("baek14503.txt")


"""
해당 작업을 끝날떄까지 진행

1. 현재 위치 청소
2. 현재 기준 왼쪽방향 아직 방문 안한 곳 존재 하면
   => 회전 후 그 칸으로 이동 후 1번 (그 칸 청소)
   (이걸 현재 칸 기준 왼쪽 방향으로 (counter-clockwise) 탐색하여 방문안한 칸 있을때까지 탐색)
   => 현재 기준 네방향 모두 방문한 경우 
      방향 유지하며 한칸 후진, 다시 2번(현재 방향기준 왼쪽방향부터 방문 안한곳 체크)
      => 이때 만약 후진이 불가하면 동작 끝.

따라서 종료 조건
=> 모든 칸을 청소 한 경우 / 더 이상 동작이 불가한 경우
"""

def calc_clean_area(arr, start):

    r = len(arr)
    c = len(arr[0])
    
    # 0  1  2  3
    # 북 서 남 동  (왼쪽 방향 탐색)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    
    # 청소 할 수 있는 최대 영역 체크
    total_area = 0
    for i in range(0, r):
        for j in range(0, c):
            if arr[i][j] == 0:
                total_area += 1

    visited = [[False] * c for _ in range(0, r)]

    row, col, direct = start
    # 벡터함수 편의상 초기 방향값 조정 (서, 동만 반대로 바꾸면 됨 1-> 3, 3 -> 1)
    if direct == 1 or direct == 3:
        direct = (direct+2) % 4

    visited[row][col] = True
    area = 1

    while area < total_area:

        flag = False
        for k in range(1, 5):
            # 현재 기준 왼쪽방향부터 탐색 (현재 방향 벡터함수에서 1씩 빼주는게 왼쪽방향 회전이 됨)
            d = (direct+k) % 4 
            next_row = row + dr[d]
            next_col = col + dc[d]

            # 벽이면 pass (테두리를 감싸고 있는 문제라서, map 영역 벗어나는것 걱정할 필요 X)
            if arr[next_row][next_col]:
                continue
            # 이미 방문
            if visited[next_row][next_col]:
                continue
            # 청소 가능하면 이동해서 청소후 다음 반복 진행
            flag = True
            visited[next_row][next_col] = True
            area += 1
            row = next_row
            col = next_col
            direct = d
            break
        # 현재 기준 청소할 곳이 없는 경우, 현재 방향으로 1칸 후진 
        if not flag:
            d = (direct+2) % 4
            next_row = row + dr[d]
            next_col = col + dc[d]
            # 후진 불가하면 작업 종료
            if arr[next_row][next_col]:
                break
            # 만약 청소 안했으면 청소, 아니면 그냥 후진만, 방향은 유지해야함
            if not visited[next_row][next_col]:
                area += 1
                visited[next_row][next_col] = True
            row = next_row
            col = next_col
    return area


N, M = map(int, input().split())
start = list(map(int, input().split()))
MAP = [[0] * M for _ in range(0, N)]
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))


answer = calc_clean_area(MAP, start)
print(answer)