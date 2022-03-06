"""
전형적인 DFS 문제
3장고르는걸 DFS 돌리고, 숫자 M을넘으면 가지치기
그 안에서 최댓값 고르면 됨. depth를 3까지만가져가므로 충분히 가능
"""

import sys
sys.stdin = open("baek2798.txt")


def dfs(n, sum, numbers, limit, check):
    global maximum
    if n == 3:
        if sum >= maximum:
            maximum = sum
        return
    for i in range(0, len(numbers)):
        # 이미 고른 카드면 pass
        if check[i]:
            continue
        next = sum + numbers[i]
        # 합이 정해진 limit을 넘긴 경우도 pass
        if next > limit:
            continue
        # 가능한 경우에 대한 dfs 진행
        check[i] = True
        dfs(n+1, next, numbers, limit, check)
        check[i] = False
    

N, M = map(int, input().split())
NUMS = list(map(int, input().split()))
visited = [False] * len(NUMS)
maximum = 0
dfs(0, 0, NUMS, M, visited)
print(maximum)