import sys
sys.stdin = open("baek1043.txt")

"""
union find 에서 루트 노드를 찾을떄는 
parent 배열을 쓰는게아니라
find 메서드를 써야한다 이부분 주의!!!
"""


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
    person.sort()
    head = person[0]
    for i in range(0, len(person)-1):
        for j in range(i+1, len(person)):
            union(person[i], person[j])
    P = [0] * M
    for i in range(0, M):
        party = list(map(int, input().split()))
        P[i] = party[1:]
        if party[0] > 1:
            temp = party[1:]
            for j in range(0, len(temp)-1):
                for k in range(j+1, len(temp)):
                    union(temp[j], temp[k])

    ban_list = []
    # 루트 노드 업데이트
    head_p = find(head)
    for i in range(1, N+1):
        # ban_list 작성
        if find(i) == head_p:
            ban_list.append(i)
    for i in range(0, len(P)):
        flag = True
        for j in range(0, len(P[i])):
            if P[i][j] in ban_list:
                flag = False
                break
        # ban_list에 전부 없는 경우만 정답
        if flag:
            answer += 1
print(answer)