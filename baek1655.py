import sys
import heapq
sys.stdin = open("baek1655.txt")

"""
중앙값보다 큰 위치는 최소힙으로 (right)
중앙값 이하의 인덱스 위치는 최대힙으로 저장! (left)

기본적으로는 left => right 순으로 번갈아가면서 push 하면서
left의 0번 값이 right의 0번값보다 큰수가 들어간다면 위치를 교환해주어야한다
(중앙값이 바뀐 조건)
"""

N = int(sys.stdin.readline())

# 최대힙 (중앙값 이하 인덱스 친구들)
left_hand = []
# 최소힙 (중앙값보다 큰 인덱스 친구들)
right_hand = []

time = 0
for i in range(0, N):
    # 최대힙, 최소힙에 번갈아가면서 push
    num = int(sys.stdin.readline())
    if time % 2:
        heapq.heappush(right_hand, num)
    else:
        heapq.heappush(left_hand, -num)

    # 만약 최소힙이 있는경우에, -최대힙의 0번 인덱스 값 > 최소힙 0번 인덱스 값인 경우가 있으면
    # 중앙값이 변한것, 최대힙 , 최소힙 0번값을 서로 교환해준다.
    # 항상 최대힙의 0번인덱스값을 부호 바꾸어주면 그게 중앙값
    if right_hand and right_hand[0] < -left_hand[0]:
        # 최소힙에서 가져옴
        tmp1 = heapq.heappop(right_hand)
        # 최대힙에서 가져옴
        tmp2 = heapq.heappop(left_hand)
        # 서로를 교환
        heapq.heappush(right_hand, -tmp2)
        heapq.heappush(left_hand, -tmp1)
    time += 1
    print(-left_hand[0])
