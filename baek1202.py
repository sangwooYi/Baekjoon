import sys
import heapq
sys.stdin = open('baek1202.txt')

"""
전략1.  ===> 얘도 시간 초과나네...

가방 무게 오름차순 정렬 + ptr로 위치 도입

보석도 무게 오름차순 정렬, 같은 무게에 대해서는 가치 내림차순

=> 보석에 대해 순회 시작
ptr < 가방갯수, 보석의 무게 <= 가방[ptr]의 무게:
: 바로 담을 수 있는경우, 담고 heapq에 저장 (가치, 무게, 담은 가방 ptr) 로 저장

ptr >= 가방갯수 or 보석 무게 > 가방[ptr]의 무게 인 경우:
: 담을 수 없는 경우임   => 여기를 어떻게 해야할것같은데..?
힙큐에 자료 없으면 => 그냥 pass해야 되는 상황 (그냥 못담는거다)
힙큐에 자료 있으면
=> pop, 현재 담고있는 보석중 최소 가치 순으로 pop된다.
=> 1. 그 가방에 현재 보석을 담을 수 있다면
=> 가치 비교 후 더 가치가 높으면 교체, 낮으면 그냥 pass (가방의 담긴 보석중 최소가치보다도 낮은거니가)
=> 2. 담을 수 없는 경우면, 담을 수 있는 가방 나올 때까지 pop 진행(그 전 pop한 애들은 우선 que에 임시저장)
=> 작업 마친 이후, 임시 큐에 있는 애들이 있다면 다시 heapq에 push 해 준다.


전략2.
오히려 가방을 순회
1. 현재 무게에 대해, 담을 수 있는 가방을 무게 순으로 최대힙 저장
2. 그 후, 최대힙에 있는 자료가 있다면, 그 중 최대 무게의 보석만 현재 가방에 저장
3. 이 작업을 끝날때까지 반복!
"""



N, K = map(int, input().split())
jewels = [0] * N
for i in range(0, N):
    jewels[i] = list(map(int, sys.stdin.readline().split()))
bags = [0] * K
for i in range(0, K):
    bags[i] = int(sys.stdin.readline())

# 보석, 가방 둘다 무게 오름차순으로 정렬
jewels.sort()
ptr = 0
bags.sort()


temp = []
answer = 0
for i in range(0, K):
    now = bags[i]

    # 보석이 남아있는 한에서, 가방에 담을 수 있는 보석 전부 temp에 저장
    while ptr < N and jewels[ptr][0] <= now:
        w, v = jewels[ptr]
        ptr += 1
        heapq.heappush(temp, -v)
    # temp에 저장된 보석이 있다면, 현재 가방에 temp에 보석중 최대 무게의 보석을 저장
    # 그러면 현재 가방에는 가능한 최대의 가치가 들어가게 된것!
    if temp:
        value = -heapq.heappop(temp)
        answer += value
print(answer)

