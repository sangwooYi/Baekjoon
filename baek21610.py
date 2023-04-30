import sys
sys.stdin = open("baek21610.txt")

"""
그냥 빡구현 문제

1. 우선 d 방향으로 s만큼 구름이 이동
=> s가 최대 50이기 떄문에 1바퀴 이상이 넘어갈일은 없음
따라서 영역이 넘어갈 때 현재 열 위치가 r 일 때
(r+N+s)%N
2. 구름이 있는 칸에는 물이 1증가하며 구름 사라짐 (구름 위치 체크해 두어야 함)
3. 구름이 있던 영역은 각 대각선 거리가 1인 칸중 물이 있는 칸 수 만큼 물의 양 증가
    (영역 벗어나거나 물의양 0이면 제외)
4. 구름이 있던 영역을 제외하고, 나머지 영역 중 물의양이 2 이상인 곳에서 구름 생성

이걸 M번 만큼 반복!
"""

#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# N은 맵 크기 M은 명령 갯수
N, M = map(int, input().split()) 
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

# 구름이 있는 포인트만 체크 or 구름있는 위치를 표기하는 맵 사용
# 우선 1번으로
cloud_points = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
for t in range(0, M):
    d, s = map(int, input().split()) 
    # 다음 순회 때 구름 정보 저장 용
    tmp_arr = []
    # 구름 위치 체크 및, 물복사량 저장 용
    cloud_check = [[-1] * N for _ in range(0, N)]
    for i in range(0, len(cloud_points)):
        cur_r, cur_c = cloud_points[i]
        # 인덱스 처리
        next_r = (cur_r + (dr[d-1]*s) + N)%N
        next_c = (cur_c + (dc[d-1]*s) + N)%N
        
        # 구름으로 인해 물의 양 1 증가
        MAP[next_r][next_c] += 1
        cloud_points[i] = [next_r, next_c]

  
    # 대각선 거리 1에 있는 칸 중 물이 있는 칸만큼 증가
    # 델타함수에서 인덱스 기준 1, 3 , 5, 7
    for i in range(0, len(cloud_points)):
        chk_cnt = 0
        row, col = cloud_points[i]
        for j in range(1, 8, 2):
            # 대각선 거리 1만큼
            chk_row = row + dr[j]
            chk_col = col + dc[j]
            if chk_row < 0 or chk_col < 0 or chk_row >= N or chk_col >= N:
                continue
            # 물이 있는경우만
            if MAP[chk_row][chk_col]:
                chk_cnt += 1
        cloud_check[row][col] = chk_cnt
    # 물복사
    for i in range(0, len(cloud_points)):
        row, col = cloud_points[i]
        MAP[row][col] += cloud_check[row][col]

    # 다음 구름 생기는곳 체크
    for r in range(0, N):
        for c in range(0, N):
            # 이전단계에서 구름이 없었고, 물의 양이 2 이상인곳 물양 2감소하며 구름 생성
            if cloud_check[r][c] == -1 and MAP[r][c] >= 2:
                MAP[r][c] -= 2
                tmp_arr.append((r, c))
    cloud_points = tmp_arr


total_water = 0
for r in range(0, N):
    for c in range(0, N):
        total_water += MAP[r][c]
print(total_water)