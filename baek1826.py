import sys
import heapq
sys.stdin = open("baek1826.txt")

"""
현재 연료 량으로 갈 수 있는 주유소중
가장 많은 기름을 채울 수 있는 곳을 찾아야한다.
"""

def calc_stop_point(info, end, init):
    # 0번부터 시작
    point = 0
    hq = []
    # 처음부터 도착할 수 있는 경우
    if init >= end:
        return 0
    count = 0
    gas = init
    while point < end:
        if point + gas >= end:
            return count
        # 이동 가능한 범위 내에서 전부 체크
        while info:
            now = info[0]
            #  내가 가진 연료량으로 이동 가능할 경우에만
            if (now[0] - point) <= gas:
                dist, fuel = heapq.heappop(info)
                # 최대힙으로 
                heapq.heappush(hq, (-fuel, dist))
            # 안되는 경우는 바로 break
            else:
                break
        # 현재 hq에 저장된 최대 값을 사용한다.
        if hq:
            next_gas, next_point = heapq.heappop(hq)
            # 이동거리만큼 기름 소모
            gas -= (next_point-point)
            # 최대힙을 위해 음수로 저장했으므로 오히려 빼줘야 함
            gas -= (next_gas)
            point = next_point
            count += 1
        # hq가만약에 비어있다면
        else:
            # 현재 연료량으로 목적지까지 못하는 경우면 도착 못하는 case
            if point + gas < end:
                return -1
            # 아니라면 그냥 다음 반복으로 진행

N = int(input())
# 단순 탐색하는것 자체는 dict가 더 효율적임
infos = []
for i in range(0, N):
    # point, 연료 충전량
    a, b = map(int, input().split())
    heapq.heappush(infos, (a, b))
L, P = map(int, input().split())

answer = calc_stop_point(infos, L, P)
print(answer)