import sys
from collections import deque
sys.stdin = open("baek17071.txt")

"""
짝수시간 / 홀수시간 나누어서 visited 체크하는 아이디어 진짜...
반드시 다시한번 풀어보자!

사고능력이 한번더 확장되어야 함!
"""


N, K = map(int, input().split())
upper_bound = 500000
lower_bound = 0
visited = [[-1] * (upper_bound+1) for _ in range(0, 2)]

# 우선 bfs로 전부 시간체크 500000*2
def bfs(n):
    que = deque()

    # 해당 위치에 짝수 최소시간, 홀수 최소시간을 체킹한다
    # -1, +1 // +1 , -1 을하면 다시 원래 위치로 올 수 있기 때문!!
    # visited의 사용 목적을 잘 기억하자! T/F로만 할게아니고, 문제의 필요에 따라
    # visited 방문체크 로직을 얼마든지 바꿀 수 있어야 한다!
    visited[0][n] = 0
    que.append((n, 0))

    while que:
        now, time = que.popleft()
        flag = time%2

        # 이방법도 깔끔한듯!
        next_nows = [now-1, now+1, now*2]

        for next_now in next_nows:
            if next_now < lower_bound or next_now > upper_bound:
                continue
            # 방문처리가 안된 지역만
            if visited[1-flag][next_now] == -1:
                visited[1-flag][next_now] = time+1
                que.append((next_now, time+1))

bfs(N)
# 그다음에 K를 늘려보면서 방문 가능한지 체크
# 여기서 포인트는 현재 K가 방문한 해당 visited 위치에서의 시간이
# visited에 체크된 최소시간 이후이기만 하면, 반드시 잡을 수 있다는 부분!
# 방문한뒤에, -1 / +1  혹은 +1 -1 을 통해 2초뒤면 다시 제자리로 올 수 있기때문
# 이때문에 visited를 홀수시간 / 짝수시간을 구분해서 체킹한것!!@!
t = 0
flag = 0
answer = -1

while K <= upper_bound:
    # 방문한 지점중에서만
    if visited[flag][K] == -1:
        continue
    if visited[flag][K] <= t:
        answer = t
        break
    flag = 1-flag  # 0이면 1 1이면 0
    t += 1
    K += t
print(answer)