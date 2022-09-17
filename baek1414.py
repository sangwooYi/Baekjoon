import sys
sys.stdin = open("baek1414.txt")

"""
크루스칼 사용

(출발 노드 정해져있으면 프림, 아니면 크루스칼!)
"""

def find(x):
    if parent[x] == x:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)
    if px <= py:
        parent[py] = px
    else:
        parent[px] = py 


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

# 실제로는 아스키코드가 A는 65, Z는 90,  a는 97, z는 122이다
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

conv_alph_to_val = {}
val = 1
for i in range(a, z+1):
    conv_alph_to_val[chr(i)] = val
    val += 1
for i in range(A, Z+1):
    conv_alph_to_val[chr(i)] = val
    val += 1

edge_cost = [[0] * N for _ in range(0, N)]
total_cost = 0
for r in range(0, N):
    for c in range(0, N):
        if MAP[r][c] == '0':
            edge_cost[r][c] = 0
        else:
            val = conv_alph_to_val[MAP[r][c]]
            edge_cost[r][c] = val
            total_cost += val


parent = [i for i in range(0, N)]
edges = []
for r in range(0, N):
    for c in range(0, N):
        if r != c and edge_cost[r][c]:
            edges.append((r, c, edge_cost[r][c]))

edges.sort(key=lambda x : x[2])

min_req = 0
for edge in edges:
    s, e, cost = edge

    if find(s) != find(e):
        union(s, e)
        min_req += cost


root = find(0)
flag = True
for i in range(1, N):
    # 모든 연결이 안된 경우
    if find(i) != root:
        flag = False
        break
if flag:
    print(total_cost-min_req)
else:
    print(-1)