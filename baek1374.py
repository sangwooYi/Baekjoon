import sys
import heapq
sys.stdin = open("baek1374.txt")


"""
시작시간 정렬 후, 우선순위 큐는 종료시간 기준,

== 이 로직 꼭 기억하자 ===
1. hq 없으면 무조건 push
2. 아니라면
=> 현재 hq에서 가장 빠른 종료시간 (heapq는 최소힙이다. ) <= schedules 배열에 시작시간
   이라면, 강의실을 늘릴 이유 X 따라서, heappop 후 heappush
=> 아니라면, 강의실이 추가 필요
"""


N = int(sys.stdin.readline())
schedules = [0] * N
for i in range(0, N):
    n, a, b = map(int, sys.stdin.readline().split())
    schedules[i] = (n, a, b)
schedules.sort(key=lambda x : x[1])

hq = []
for i in range(0, N):
    n, a, b = schedules[i]
    if not hq:
        heapq.heappush(hq, b)
    else:
        # 현재 배정 된 강의중 가장 빠른 종료 시간 <= 배정해야할 강의 시작시간
        if hq[0] <= schedules[i][1]:
            heapq.heappop(hq)
        heapq.heappush(hq, b)
print(len(hq))