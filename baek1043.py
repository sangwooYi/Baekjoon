import sys
sys.stdin = open("baek1043.txt")


def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)
    # 작은쪽으로 합체
    if px < py:
        parent[py] = px
    else:
        parent[px] = py
    
N, M = map(int, input().split())
parent = [i for i in range(0, N+1)]

know = list(map(int, input().split()))
answer = 0
if know[0] == 0:
    answer = M
else:
    person = know[1:]
    head = person[0]
    for i in range(0, len(person)):
        union(person[0], person[i])

    P = [0] * M
    for i in range(0, M):
        party = list(map(int, input().split()))
        P[i] = party[1:]
        if party[0] > 1:
            temp = party[1:]
            for j in range(0, len(temp)-1):
                for k in range(j, len(temp)):
                    union(parent[temp[j]], parent[temp[k]])

    ban_list = []
    head_p = parent[head]
    
    for i in range(1, N+1):
        if parent[i] == head_p:
            ban_list.append(i)
    for i in range(0, len(P)):
        flag = True
        for j in range(0, len(P[i])):
            if P[i][j] in ban_list:
                flag = False
                break
        if flag:
            answer += 1
print(answer)