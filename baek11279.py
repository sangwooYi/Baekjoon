import sys
import heapq
sys.stdin = open("baek11279.txt")




N = int(sys.stdin.readline())
hq = []
for i in range(0, N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(hq) == 0:
            print(0)
        else:
            now = heapq.heappop(hq)
            print(-now)
    else:
        # 기본적으로 heapq는 최소힙 따라서 최대힙으로 쓸때는 아래와같이 트릭 사용
        heapq.heappush(hq, -X)
       