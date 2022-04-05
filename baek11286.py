import sys
import heapq
sys.stdin = open("baek11286.txt")


N = int(input())
hq = []
for i in range(0, N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            now = heapq.heappop(hq)
            if now[1] == 1:
                print(now[0])
            elif now[1] == 0:
                print(-now[0])
    elif x > 0:
        heapq.heappush(hq, (x, 1))
    else:
        heapq.heappush(hq, (-x, 0))
