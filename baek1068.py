import sys
sys.stdin = open("baek1068.txt")

"""
반례를 혼자서 생각해 낼 수 있어야 한다!!
이 부분이 진짜 사고력임!!
"""

def dfs(node):
    global cnt
    # 삭제노드이면 진행 하면 안됨
    if node == remove_node:
        return
    # 리프 노드
    if len(trees[node]) == 0:
        cnt += 1
        return
    flag = False
    for child in trees[node]:
        # 자식으로 진행
        if child == remove_node:
            continue
        flag = True 
        dfs(child)
    # 만약 현재 노드의 리프노드가 제거되어, 현재 노드가 리프가 되는경우도 존재!
    if not flag:
        cnt += 1       



N = int(input())
nodes = list(map(int, input().split()))
remove_node = int(input())
cnt = 0
trees = [[] for _ in range(0, N)]

root = 0
for i in range(0, N):
    parent = nodes[i]
    if parent != -1:
        trees[parent].append(i)
    else:
        root = i
dfs(root)
print(cnt)
