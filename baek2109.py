import sys
import heapq
sys.stdin = open("baek2109.txt")

"""
전략.

정렬은 남은 날짜 오름차순, 같은 날짜중에서는 점수 큰 순으로 정렬.
현재 값이 day <= 남은 날짜 이면 heappush
여기서 중요한것은 (점수, 날짜) 형태로 push하는 것이다.

day > 남은 날짜이면 heappop
그러면 현재 갖고 있는 강의중 가장 낮은 값이 튀어나옴
=> 그 값과, 현재 내가 가리키고 있는 값중 더 큰 값을 push

아래 로직에서 else부분을 안 밟으면, 현재 가까운 날짜의 강의를 선택하느라 더 큰 페이를 놓칠 수 있다.
반례, else 로직이 없으면 이런 경우에 [10, 20, 80]을 담는다. 하지만 실제로는 [20, 80, 50] 을 선택해야함
 p  d
10  1
20  2
80  3
50  3

if day <= 남은날짜:
    heapq.heappush(hq, p)
else:
    temp = heapq.heappop(hq)
    select = max(temp, p)
    heapq.heappush(hq, select)
"""


N = int(input())
P = [0] * N
for i in range(0, N):
    P[i] = list(map(int, input().split()))

P.sort(key=lambda x : (x[1], -x[0]))

answer = 0
day = 1
hq = []
for i in range(0, len(P)):
    p, d = P[i]
    if d >= day:
        heapq.heappush(hq, p)
        day += 1
    # p < d
    else:
        # (현재 저장된 강의 list 중 가장 낮은 pay vs 현재 가리키는 pay) 중 더 큰 값을 선택
        temp = heapq.heappop(hq)
        select = max(temp, p)
        heapq.heappush(hq, select)
for i in range(0, len(hq)):
    answer += hq[i]
print(answer)