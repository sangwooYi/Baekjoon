import sys
sys.stdin = open("baek11047.txt")

"""
오름차순으로 주어지니까 정렬할 필요도 X
그냥 그리디 기본문제
"""


def find_min_req(goal, coins):
    count = 0
    idx = len(coins) - 1
    res = goal

    while res > 0:
        # 현재 남은 잔액이 coin 가치보다 낮을 때
        if res < coins[idx]:
            idx -= 1
            continue
        amount = res // coins[idx]
        res = res % coins[idx]
        count += amount
    return count


N, K = map(int, input().split())
A = [0] * N
for i in range(0, N):
    A[i] = int(input())
ans = find_min_req(K, A)
print(ans)