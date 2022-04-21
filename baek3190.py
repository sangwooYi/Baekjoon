import sys
sys.stdin = open("baek3190.txt")
"""
아이디어, 출발은 우측방향 즉 dr[0], dc[0]

그 후 만약 오른쪽 회전("D")
은 (dir + 1) % 4
왼쪽회전은 (dir - 1) % 4

매번 해당 방향으로 한칸씩 전진. 
뱀의 머리를 포함한 몸통, 꼬리는 각각 좌표, 방향(dir)변수를 갖고 있음
매초마다 머리는 한칸씩 dir변수 방향으로 이동,
꼬리는 머리가 도착한 곳이 사과가 없으면 dir변수방향으로 이동
위 처리를 위해 머리와 꼬리 좌표는 항상 따로 갖고 있어야 함.

만약 머리가 이동한 방향이 맵을 벗어나거나 or 뱀 자기자신좌표에 다다르면 게임종료.

문제 잘 읽자!!
"""

def snake_game(arr, rotate, n):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    check = [[False] * n for _ in range(0, n)] 
    # 뱀의 공간차지여부, 꼬리가 이동할때 가야할 방향을 담는 것으로
    check[0][0] = (1, 0)
    # row, col, 방향
    snake_head = (0, 0, 0)
    snake_tail = (0, 0)

    time = 0    
    while True:
        row, col, dir = snake_head

        if time in rotate.keys():
            if rotate[time] == "L":
                dir = (dir-1) % 4
            elif rotate[time] == "D":
                dir = (dir+1) % 4 
            # check도 바꿔줘야함
            check[row][col] = (1, dir)
        next_row = row + dr[dir]
        next_col = col + dc[dir]
        next_time = time+1
        # 맵 밖으로 벗어날때
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            return next_time
        # 뱀 자기 자신과 충돌한 경우
        if check[next_row][next_col]:
            return next_time
        
        # 사과가 있는 경우 그냥 머리만 전진
        check[next_row][next_col] = (1, dir)
        snake_head = (next_row, next_col, dir)
        # 사과가 없는 경우만 체크하면 됨
        if arr[next_row][next_col] == 0:
            tail_row, tail_col = snake_tail
            # 사과 없으면 꼬리가 이동해야함
            tail_dir = check[tail_row][tail_col][1]
            check[tail_row][tail_col] = 0
            next_tail_row = tail_row + dr[tail_dir]
            next_tail_col = tail_col + dc[tail_dir]
            next_tail_path = check[next_tail_row][next_tail_col][1]
            snake_tail = (next_tail_row, next_tail_col)
        # 사과 있었으면 먹는것! 따라서 사과를 없애줘야함!
        else:
            arr[next_row][next_col] = 0

        time = next_time


N = int(input())
K = int(input())
MAP = [[0] * N for _ in range(0, N)]
for i in range(0, K):
    # 사과 위치 체크
    r, c = list(map(int, input().split()))
    # 가장 좌상단 좌표가 1,1으로 시작하는 문제이므로 인덱스 처리
    MAP[r-1][c-1] = 1
L = int(input())
rot_dict = {}
for i in range(0, L):
    # x 초가 끝난 뒤
    x, c = input().split()
    rot_dict[int(x)] = c

ans = snake_game(MAP, rot_dict, N)
print(ans)