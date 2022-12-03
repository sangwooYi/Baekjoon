import sys
from collections import deque
sys.stdin = open("baek18235.txt")


"""
같은 지점에 똑같은 방향으로 또 도착해야 하는 경우도 존재!
따라서 방향으로 구분도 안된다. 
=> 그냥 해당 지점에 며칠에 도착하는지만 체크 후, B가 그 날짜에 해당 지점에 도착할 수 있는지 확인
(어차피 2**19 == 51만이므로 최대 18일까지만 진행되므로 가능한것!)

"""

def find_min_day(n, a, b):
    # 2**i <= n 인 범위까지 미리 계산 (2**19 이 약 51만 N은 최대 50만까지)
    pos_range_of_date = [0, 1]
    tmp = 1
    while True:
        tmp *= 2
        if tmp >= n:
            break
        pos_range_of_date.append(tmp)
    limit_date = len(pos_range_of_date)

    visited = [[False]*limit_date for _ in range(0, n+1)]

    que = deque()
    # a 먼저 진행
    que.append((a, 1))
    while que:
        a_pos, days = que.popleft()
        move_range = pos_range_of_date[days]
        for k in range(-1, 2, 2):
            next_a = a_pos + (k*move_range)
            if next_a <= 0 or next_a > n:
                continue
            visited[next_a][days] = True
            if days == limit_date-1:
                continue
            que.append((next_a, days+1))
    
    que.append((b, 1))
    while que:
        b_pos, days = que.popleft()
        move_range = pos_range_of_date[days]
        for k in range(-1, 2, 2):
            next_b = b_pos + (k*move_range)
            if next_b <= 0 or next_b > n:
                continue
            # a와 같은날짜에 같은 지점에 도착할 수있으면 바로 종료
            if visited[next_b][days]:
                return days
            if days == limit_date-1:
                continue
            que.append((next_b, days+1))
    return -1

N, A, B = map(int, input().split())


answer = find_min_day(N, A, B)
print(answer)