import sys
sys.stdin = open("baek17144.txt")

"""
아니 왜틀리는건데 ㅡㅡ?
R은 row (행) C는 col(열)  T 는 time(시간)
확산은 가능한 모든방향으로 확산 a/5 만큼 확산되고, 버림이다 (그냥 int하면 되긴함)
포인트는, 확산이 중첩적으로 이루어질때 처리를 어떻게 하는지가 포인트
확산 불가능한건 벽(MAP 밖일때), 공기청정기 (-1 좌표)
(우선 현재 칸기준으로 계산될 애들을 우선 저장만 해둔 뒤에 한번에 처리하는게 맞을듯?)


공기청정기 작동시에는 위쪽은 반시계 아랫쪽은 시계방향
미세먼지가 바람의 방향대로 모두 한칸씩 이동, 그 전칸은 깨끗해짐

매초 위 동작이 반복되는것

위같은 문제는 일단 한번 cycle을 제대로 구현하고 그다음 반복을 시키는 순서로 진행

최대 50 x 50이므로 완전탐색 반복해도 충분히 가능

이따 추가로 풀어보자
"""


def after_purify(crds, r, c, t):
    purify_up = 0
    purify_down = 0
    # 위 아래 왼 오
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(0, r):
        # 무조건 연결되어있다. 따라서 아래처럼 체크
        if crds[row][0] == -1:
            purify_up = row
            purify_down = row+1
            break
    time = 0
    while time < t:
        time += 1
        # 해당 좌표의 변화값을 바로 반영안하고 임시로 저장하는 곳
        temp_box = [[0] * c for _ in range(0, r)]
        for row in range(0, r):
            for col in range(0, c):
                # 공기 청정기 pass
                if crds[row][col] == -1:
                    continue
                # 미세먼지 있는 곳에서 네방향 탐색 진행
                if crds[row][col] != 0:
                    temp_sum = 0
                    now = crds[row][col]
                    for dir in range(0, 4):
                        next_row = row + dr[dir]
                        next_col = col + dc[dir]
                        # 아래 한조건이라도 해당되면 pass 따라서 or
                        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                            continue
                        # 공기 청정기라도 pass
                        if crds[next_row][next_col] == -1:
                            continue
                        # 확산 가능한 곳
                        dif = now // 5
                        temp_box[next_row][next_col] += dif
                        temp_sum += dif
                    temp_box[row][col] -= temp_sum
        # 좌표별로 계산되어야 할 값들이 저장되어있으므로 반영
        for row in range(0, r):
            for col in range(0, c):
                val = temp_box[row][col]
                crds[row][col] += val
        # 공기 청정기 가동 역시 임시 좌표 활용
        temp_box = [[0] * c for _ in range(0, r)]   
        # 얘는 한번에 처리
        for col in range(0, c-1):
            # 왼방향으로
            temp_box[0][c-col-2] = crds[0][c-1-col] 

            temp_box[r-1][c-col-2] = crds[r-1][c-1-col]
            # 오른방향으로
            # 공기 청정기 pass
            if col == 0:
                continue
            temp_box[purify_up][col+1] = crds[purify_up][col]
            temp_box[purify_down][col+1] = crds[purify_down][col]

        # 얘는 따로
        for row in range(0, purify_up):
            # 위방향
            temp_box[purify_up-row-1][c-1] = crds[purify_up-row][c-1]
            # 아래 방향, 공기청정기로 이동하는 쪽은 그냥 사라져버리는것
            if row == purify_up-1:
                continue
            temp_box[row+1][0] = crds[row][0]

        for row in range(purify_down, r-1):
            # 아래방향
            temp_box[row+1][c-1] = crds[row][c-1]

        # 위방향    
        # 어차피 purify_down+2까지만 봐야한다.
        for row in range(r-1, purify_down+1, -1):
            temp_box[row-1][0] = crds[row][0]
    
        # 해당 부분을 복사
        for col in range(0, c):
            crds[0][col] = temp_box[0][col]
            crds[r-1][col] = temp_box[r-1][col]
            if col == 0:
                continue
            crds[purify_up][col] = temp_box[purify_up][col]
            crds[purify_down][col] = temp_box[purify_down][col]
        for row in range(0, r):
            crds[row][c-1] = temp_box[row][c-1]
            if row == purify_up or row == purify_down:
                continue
            crds[row][0] = temp_box[row][0]
    res = 0
    for row in range(0, r):
        for col in range(0, c):
            if crds[row][col] == -1:
                continue
            res += crds[row][col]
    return res
                        
    
R, C, T = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    temp = list(map(int, input().split()))
    MAP[i] = temp

answer = after_purify(MAP, R, C, T)
print(answer)