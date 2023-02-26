import sys
sys.stdin = open("baek2512.txt")

"""
상한액을 mid로 잡고 계산했을때
총 예산 초과되면 => 탐색범위 줄인다.
아니라면 탐색범위 늘린다.
"""

N = int(input())
costs = list(map(int, input().split()))
limit_cost = int(input())

left = 1
right = max(costs)+1

while left < right:
    mid = (left+right)//2

    total_cost = 0
    for i in range(0, N):
        now_cost = costs[i]

        if now_cost > mid:
            total_cost += mid
        else:
            total_cost += now_cost
    
    if total_cost > limit_cost:
        right = mid
    else:
        left = mid+1
print(left-1)