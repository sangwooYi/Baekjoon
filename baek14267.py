import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek14267.txt")


def dfs(node, amount):

    for next_node in trees[node]:
        compliment_amount[next_node] += amount
        dfs(next_node, compliment_amount[next_node])


N, M = map(int, sys.stdin.readline().split())
trees = [[] for _ in range(0, N+1)]
arr = list(map(int, sys.stdin.readline().split()))
compliment_amount = [0] * (N+1)
for i in range(0, M):
    node, amount = map(int, sys.stdin.readline().split())
    # 한 사람에게 여러번 칭찬할 수도 있다.
    compliment_amount[node] += amount
# 1번은 가장 상사임 (상사는 자기보다 번호가 작다는게 조건)
for i in range(1, N):
    node = arr[i]
    trees[node].append(i+1)

dfs(1, 0)
print(" ".join(map(str, compliment_amount[1:])))