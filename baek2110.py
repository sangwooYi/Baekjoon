import sys
sys.stdin = open("baek2110.txt")

"""
매개변수 탐색
: 이진탐색에서 조건을 만족하는 최대/최솟값을 찾는 것!


여기서는 가장 인접한 공유거리가 최대가 되는 조건을 찾아야함!
가장 인접한 공유기 거리가 mid
=> 이걸로 C개를 설치 가능? => pl 을 mid로 (좀 더 큰범위에서 탐색해본다.) + 현재 mid값을 answer에 저장
=> 설치 불가능? => pr을 mid로  (좀 좁은 범위에서 탐색해 본다.)

이진탐색 은근히 많이나옴!! 이 로직에 익숙해지자
"""


N, C = map(int, sys.stdin.readline().split())
points_dict = {}
points = [0] * N
for i in range(0, N):
    point = int(sys.stdin.readline())
    points[i] = point
    points_dict[point] = 1
points.sort()

pl = 1
# 최대 거리
pr = 1000000000
answer = 0

while pl <= pr:
    # 가장 인접한 공유기의 거리 (이 거리보다 짧은 공유기 거리가 존재하면 안됨)
    # 이거리보다 짧은 경
    mid = (pl + pr) // 2
    # 가능한 최인접거리를 줄여야 하므로 이렇게 시작?
    count = 1
    now = points[0]
    idx = 1
    while idx < N:
        # 공유기를 놓을 위치와, 직전 공유기 위치 거리가 mid 이상일경우는 공유기 설치
        if (points[idx] - now) >= mid:
            now = points[idx]
            count += 1
            # N개 설치 가능하면 더 볼필요 없다.
            if count == N:
                break
        # 아니면 다음 위치를 탐색
        idx += 1
    # 설치 가능? 범위를 더 키워보자
    if count >= C:
        answer = max(mid, answer)
        pl = mid + 1
    # 설치 불가? 범위를 좁혀보자.
    else:
        pr = mid - 1
print(answer)



            