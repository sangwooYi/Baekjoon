import sys
import heapq
sys.stdin = open("baek1927.txt")

"""
최소힙, 최대힙을 써야할때는 그냥 
heapq 사용하자!

시간나면 최소힙, 최대힙 파이선으로 한번 구현해보자
그리고 heapq는
push , pop될때마다 heapify 진행하는방식으로 구현하면 될듯? 
"""


N = int(sys.stdin.readline())
hq = []
for i in range(0, N):
    now = int(sys.stdin.readline())
    if now == 0:
        if len(hq) == 0:
            print(0)
        else:
            ans = heapq.heappop(hq)
            print(ans)
    else:
        heapq.heappush(hq, now)
    