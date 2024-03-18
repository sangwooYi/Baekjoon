import sys
import heapq
sys.stdin = open("baek19598.txt")


N = int(sys.stdin.readline())
schedules = [0] * N
for i in range(0, N):
    a, b = map(int, sys.stdin.readline().split())
    schedules[i] = (a, b)


schedules.sort()

hq = []
for i in range(0, N):
    s, e = schedules[i]
    if not hq:
        heapq.heappush(hq, e)
    else:
        # 현재 강의실에서 가장 빠른 종료시간 <= 다음 배정할 강의 시작시간
        if hq[0] <= s:
            heapq.heappop(hq)
        heapq.heappush(hq, e)
print(len(hq))