import sys
sys.stdin = open("baek4195.txt")


def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        parent[py] = px
        # 이렇게 매번 분리집합으로 묶이는 크기를 저장
        DP[px] += DP[py]
    else:
        parent[px] = py
        # 이렇게 매번 분리집합으로 묶이는 크기를 저장
        DP[py] += DP[px]

T = int(sys.stdin.readline())
for tc in range(0, T):
    F = int(sys.stdin.readline())
    parent = [i for i in range(0, 2*F+1)]
    DP = [1 for _ in range(0, 2*F+1)]

    idx = 0
    man_dict = {}
    for i in range(0, F):
        man1, man2 = sys.stdin.readline().split()
        if man1 not in man_dict.keys():
            idx += 1
            man_dict[man1] = idx
        if man2 not in man_dict.keys():
            idx += 1
            man_dict[man2] = idx
        man1_idx = man_dict[man1]
        man2_idx = man_dict[man2]

        if find(man1_idx) != find(man2_idx):
            union(man1_idx, man2_idx)
        
        now = find(man1_idx)
        # 이 방법을 통해서 O(N**2) 을 O(N)으로 효율화 하였음
        print(DP[now])