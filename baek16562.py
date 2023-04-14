import sys
sys.stdin = open("baek16562.txt")


def find(x):

    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    friends_cost[px-1] = min(friends_cost[px-1], friends_cost[x-1]) 
    return px

def union(x, y):
    px = find(x)
    py = find(y)

    if px <= py:
        parent[py] = px
        friends_cost[px-1] = min(friends_cost[px-1], friends_cost[py-1])
    else:
        parent[px] = py
        friends_cost[py-1] = min(friends_cost[px-1], friends_cost[py-1])


N, M, K = map(int, input().split())
friends_cost = list(map(int, input().split()))
parent = [i for i in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)

min_cost = 0
tmp_dict = {}
for i in range(1, N+1):
    pi = find(i)
    if pi not in tmp_dict.keys():
        tmp_dict[pi] = 1
        min_cost += friends_cost[pi-1]

answer = min_cost
if min_cost > K:
    answer = "Oh no"
print(answer)