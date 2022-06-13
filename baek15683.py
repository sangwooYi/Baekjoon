import sys
sys.stdin = open("baek15683.txt")

"""
8*8 이 최대크기의
CCTV도 최대 8개
그냥 무조건 브루트 포스!

6번은 벽이다!
카메라별 case
1번 => 4가지 경우 (상, 하, 좌, 우)
2번 => 2가지 경우 (좌우, 상하)
3번 => 4가지경우 (상우, 우하, 하좌, 좌상)
4번 => 4가지경우 (좌상우, 상우하, 우하좌, 하좌상)
5번 => 1가지경우 (전방향)

최악의 경우 4**8 == 2**16 => 약 6만가지
최대 8*8 size 맵이므로, 최악의경우가 40만가지 정도밖에 안나옴
걍 싹다 살펴봐도 문제 없다.
"""

def deep_copy(arr):
    r = len(arr)
    c = len(arr[0])
    result = [[0] * c for _ in range(0, r)]
    for i in range(0, r):
        for j in range(0, c):
            result[i][j] = arr[i][j]
    return result


N, M = map(int, input().split())
MAP = [[0] * M for _ in range(0, N)]
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

    # row, col
up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]
cases = [0] * 5
# 1번 카메라  상 하 좌 우 4가지
cases[0] = [[up], [down], [left], [right]]
# 2번 카메라 상하, 좌우 2가지
cases[1] = [[up, down], [left, right]]
# 3번 카메라 상우, 우하, 하좌, 좌상 4가지
cases[2] = [[up, right], [right, down], [down, left], [left, up]]
# 4번 카메라 좌상우, 상우하, 우하좌, 하좌상 4가지
cases[3] = [[left, up, right], [up, right, down], [right, down, left], [down, left, up]]
# 5번 카메라 전방향 1가지
cases[4] = [up, down, left, right]

# 카메라 번호별 경우의 수
case_idx = [4, 2, 4, 4, 1]

camera_point = []
camera_cases = []
pos_dict = {}
idx = 0
for i in range(0, N):
    for j in range(0, M):
        if MAP[i][j]:
            if MAP[i][j] < 6:
                # 카메라 위치와, 카메라 번호에 맞는 경우의 수
                num = MAP[i][j]
                camera_point.append((i, j, num))
                pos_dict[(i, j)] = idx
                idx += 1
                case = case_idx[num-1]
                tmp = [i for i in range(0, case)]
                camera_cases.append(tmp)

# 이거 itertools.product 알고리즘 그 자체이다! 
# 데카르트 곱 구현할 때 이거 쓰면 됨 이거 꼭 기억하자!
result = [[]] 
for case in camera_cases:
    result = [x + [y] for x in result for y in case]

# 데카르트 곱 알고리즘 구현할때 이거 꼭 기억! itertools.product 알고리즘임
# result = [[]]
# for pool in pools:
#     result = [x + [y] for x in result for y in pool]

min_size = N*M
for i in range(0, len(result)):
    # 이제 result[i] 에는 각 카메라 방향의 가짓수가 담겨 있음
    temp_arr = deep_copy(MAP)
    count = 0
    for j in range(0, len(result[i])):
        idx = result[i][j]
        now = camera_point[j]
        
        row = now[0]
        col = now[1]
        camera_num = now[2]
        if camera_num < 5:
            direct = cases[camera_num-1][idx]
        elif camera_num == 5:
            direct = cases[camera_num-1]
        # 각 경우별로 감시영역을 체크한뒤에 카운팅
        for k in range(0, len(direct)):
            term = 1
            rdir = direct[k][0]
            cdir = direct[k][1]
            # 범위 안에 있을 동안만
            while 0 <= row + (term*rdir) < N and 0 <= col + (term*cdir) < M:
                next_row = row + (term*rdir)
                next_col = col + (term*cdir)
                if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                    break
                # 벽이면 더이상 못 감
                if temp_arr[next_row][next_col] == 6:
                    break
                if temp_arr[next_row][next_col] == 0:
                    # 그냥 0 이 아닌값을 대입
                    temp_arr[next_row][next_col] = 9
                term += 1
    for r in range(0, N):
        for c in range(0, M):
            if temp_arr[r][c] == 0:
                count += 1
    min_size = min(min_size, count)
print(min_size)
                
