import sys
sys.stdin = open("baek17779.txt")

"""
1 <= x <= N-(d1+d2)
1+d1 < y < N-d2
범위를 순회하여 각 구역정해서 
가장 인구 많은 구역 - 가장 인구 적은 구역을 구해서
최솟값 구한다
d1 , d2도 브루트포스로 순회해야하며
d1, d2 >= 1 / 2 <= d1+d2 <= N-x 범위를 갖는다.
즉 d1 => 1 ~ N-x-1 까지 순회하며
그에 따른 d2 => 1부터 d1값이 결정되었을때 최대범위까지 각각 순회
(최대 N-1-d1)

1. d1, d2 값을 순회한다. (d1 최대 N-2까지 순회 가능 (x도 1 d2도 1))
2. 각 d1/d2에 따라 x, y (x가 행 y가 열)값을 정해서 진행
즉 4중 for문 ..
=> N이 20일때 아래 순회시 총 10,830회 연산 진행 (충분히 가능하단 소리)

x, y, d1, d2가 정해졌을때 구역 5정하는 방법
x, y => x+d1, y-d1 => x+d1+d2, y-d1+d2  
x, y => x+d2, y+d2 => x+d2+d1, y-d1+d2
우선 구역 5를 전부 체크한후
(위 방법대로 경계선 체크 후, 경계 사이에 영역 체크하는 방식)

나머지 중 아래 범위로 구역을 나눔
구역 1 => 1 <= r < x+d1 / 1 <= c <= y 
구역 2 => 1 <= r <= x+d2 / y < c <= N
구역 3 => x+d1 <= r <= N, 1 <= c < y-d+d2
구역 4 => x+d2 < r <= N, y-d1+d2 <= c <= N

진짜 그냥 주어진 대로 체크할것!
"""

# d1,d2, x, y 가 결정되었을때 구역처리
def gerrymendering(x, y, d1, d2):

    min_popular = 987654321
    max_popular = 0
    # 1번부터 5번구역 인구수 체크
    area_sum = [0] * 6
    # x, y 는 인덱스에 우선 맞춘다.
    x -= 1
    y -= 1

    check_map = [[0] * N for _ in range(0, N)]
    check_map[x][y] = 5
    check_map[x+d2+d1][y+d2-d1] = 5   
    # 5구역 체크
    for i in range(1, d1+1):
        check_map[x+i][y-i] = 5
        check_map[x+d2+i][y+d2-i] = 5
    for i in range(1, d2+1):
        check_map[x+i][y+i] = 5
        check_map[x+d1+i][y-d1+i] = 5
    
    # 사잇영역 채우기 x+1 ~ x+d1+d2-1 까지만 순회
    for r in range(x+1, x+d1+d2):
        col = 0
        while check_map[r][col] == 0:
            col += 1
        col += 1
        while col < N and check_map[r][col] == 0:
            check_map[r][col] = 5
            col += 1

    # 1번 구역
    for r in range(0, x+d1):
        for c in range(0, y+1):
            if check_map[r][c] == 0:
                check_map[r][c] = 1
    # 2번 구역
    for r in range(0, x+d2+1):
        for c in range(y+1, N):
            if check_map[r][c] == 0:
                check_map[r][c] = 2
    # 3번 구역
    for r in range(x+d1, N):
        for c in range(0, y-d1+d2):
            if check_map[r][c] == 0:
                check_map[r][c] = 3
    # 4번 구역
    for r in range(x+d2+1, N):
        for c in range(y-d1+d2, N):
            if check_map[r][c] == 0:
                check_map[r][c] = 4

    # 각 구역 총 인구수 합 
    for r in range(0, N):
        for c in range(0, N):
            cur_area = check_map[r][c]
            area_sum[cur_area] += MAP[r][c]
    
    for i in range(1, 6):
        min_popular = min(min_popular, area_sum[i])
        max_popular = max(max_popular, area_sum[i])
    return max_popular-min_popular    

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))


cur_min = 987654321
# d1은 최대 N-2까지 가능
for d1 in range(1, N-1):
    # d2는 최대 N-d1-1까지 가능
    for d2 in range(1, N-d1):
        # d1, d2 결정후 x(행), y(열) 결정
        # 최대 N-d1-d2까지 가능
        for x in range(1, N-d1-d2+1):
            # y는 1+d1 <= <= N-d2 까지 가능
            for y in range(1+d1, N-d2+1):
                cur_res = gerrymendering(x, y, d1, d2)
                cur_min = min(cur_min, cur_res)
print(cur_min)