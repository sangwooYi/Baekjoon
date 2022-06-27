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
"""



N, K = map(int, input().split())
juels = []
bags = [0] * K
for i in range(0, N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(juels, (weight, value))

for i in range(0, K):
    bags[i] = int(sys.stdin.readline())

# 보석 무게 오름차순
juels.sort()

# 가방 무게 오름차순
bags.sort()
answer = 0

tmp = []
for i in range(0, K):
    w = bags[i]
    # 담을 수 있는 보석이 있는 경우
    while juels and w >= juels[0][0]:
        now = heapq.heappop(juels)
        # 담을 수 있으면, 무게에 대해 최대 힙으로 저장
        heapq.heappush(tmp, -now[1])
    # 담을 수 있는 경우에 대해서, 최대 무게 부터 체크
    if tmp:
        answer -= heapq.heappop(tmp)
    # 만약 tmp 비어있는 상태에서 juels 가 없다면 종료 조건
    elif not juels:
        break
print(answer)