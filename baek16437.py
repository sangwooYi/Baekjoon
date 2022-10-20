import sys
sys.setrecursionlimit(2*10**5)
sys.stdin = open("baek16437.txt")

"""
트리 문제도 풀수 있어야한다.
재귀에 대해서 이해도를 높여야 함!
기본적으로 '스택' 처럼 진행된다!!
루트 노드 -> 리프 노드 순서로 재귀 진행하면 되고,
리프 노드의 정보가 알아서 부모 노드에 귀결되어 다음 부모노드로 전해짐!
"""


N = int(sys.stdin.readline())
# 리프노드에 대한 정보
tree = [[] for _ in range(0, N)]
# 현재 노드의 정보
node = [[0, 0]]
for i in range(1, N):
    w_or_s, num, link_node = sys.stdin.readline().split()
    num = int(num)
    link_node = int(link_node)-1
    # 리프 노드방향으로 트리 구성
    tree[link_node].append(i)
    node.append([w_or_s, num])

def dfs(v):
    result = 0
    # 리프 노드로 재귀 진행
    for i in tree[v]:
        # 현재 노드 기준 리프노드에 대해 재귀 진행
        result += dfs(i)
    if node[v][0] == "W":
        result -= node[v][1]
        # 현재 노드가 늑대이며, 현재까지 result가 < 0 이면 그냥 0으로
        if result <= 0:
            result = 0
    else:
        # 양이면 무조건 합산
        result += node[v][1]
    return result

answer = dfs(0)
print(answer)