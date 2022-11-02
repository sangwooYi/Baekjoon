import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek15809.txt")


def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y, code):
    px = find(x)
    py = find(y)
    # 동맹
    if code == 1:
        if px <= py:
            parent[py] = px
            A[px] += A[py]
        else:
            parent[px] = py
            A[py] += A[px]
    # 전쟁
    elif code == 2:
        if A[px] <= A[py]:
            parent[px] = py
            A[py] -= A[px]
            A[px] = 0
        else:
            parent[py] = px
            A[px] -= A[py]
            A[py] = 0

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(0, N+1)]
A = [0] * (N+1)
for i in range(1, N+1):
    A[i] = int(input())

for i in range(0, M):
    code, a, b = map(int, sys.stdin.readline().split())
    union(a, b, code)

head_dict = {}
for i in range(1, N+1):
    tmp = find(i)
    if tmp not in head_dict.keys():
        if A[tmp]:
            head_dict[tmp] = A[tmp]

head_keys = list(head_dict.keys())
answer = [head_dict[head_keys[i]] for i in range(0, len(head_keys))]
answer.sort()
print(len(head_keys))
print(" ".join(map(str, answer)))