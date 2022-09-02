import sys
sys.stdin = open("baek14621.txt")


def find(x):
    if parent[x] == x:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


N, M = map(int, input().split())
sex_ratio = list(input().split())
parent = [i for i in range(0, N+1)]
graph = [0] * M
for i in range(0, M):
    a, b, c = map(int, input().split())
    graph[i] = (a, b, c)

# sort key = lambda x : 기준 이거 잘 기억해둘것  ex key=lambda x : (x[0], -x[1]) 이런식으로 가능!
graph.sort(key= lambda x : x[2])

answer = 0
for line in graph:
    a, b, c = line
    # 간선이 성비를 다른애들만 연결해야한다.
    if sex_ratio[a-1] == sex_ratio[b-1]:
        continue

    if find(a) != find(b):
        union(a, b)
        answer += c

check = find(1)
flag = True
# 부모가 다른 노드가 존재하면 아직 최소 스패닝 트리가 만들어지지 않은것!
for i in range(2, N+1):
    if find(i) != check:
        flag = False
if flag:
    print(answer)
else:
    print(-1)