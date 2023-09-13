import sys
import heapq
sys.stdin = open("baek17503.txt")


N, M, K = map(int, sys.stdin.readline().split())
arr = [0] * K

for i in range(0, K):
    # 선호도 v, 레벨 c
    v, c = map(int, sys.stdin.readline().split())
    arr[i] = [v, c]

# 우선 난이도별로 오름차순 
arr.sort(key=lambda x : x[1])

left = 1
right = 2**31 + 1

flag = False
while left < right:

    mid = (left+right)//2
    
    hq = []
    for i in range(0, K):
        amount, level = arr[i]

        # 현재 값보다 높은 레벨이나오면 종료 (이후는 볼필요 X)
        if level > mid:
            break
        # 아직 N개 미만이면 일단 집어넣는다 
        if len(hq) < N:
            # 기본은 최소힙이다.
            heapq.heappush(hq, amount)
        else:
            # 현재 최소힙 값보다 큰경우만 교체
            if hq[0] < amount:
                heapq.heappop(hq)
                heapq.heappush(hq, amount)

    # 애초에 먹을수 있는 갯수가 부족. 따라서 값을 키워야 함
    if len(hq) < N:
        left = mid+1
        continue
    tmp_sum = 0
    for i in range(0, len(hq)):
        tmp_sum += hq[i]
    # 조건을 만족, 줄여본다
    if tmp_sum >= M:
        flag = True
        right = mid
    # 조건 불만족, 값을 더 늘려야함
    else:
        left = mid+1

if not flag:
    print(-1)
else:
    print(left)