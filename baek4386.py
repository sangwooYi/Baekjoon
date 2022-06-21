import sys
import math
sys.stdin = open("baek4386.txt")

"""
출발 노드가 정해졌다면 => 프림 (우선순위큐)
그게 아니라면 => 크루스칼!  (find, union)

일단 좌표를 decimal 이용 정수로 바꾸어서 표현
=> 계산한뒤 최종결과는 / 100 해주면 됨

조합이용해서, 두 점간의 모든 거리를 계산한다음에
크루스칼 사용
"""

def calc_distance(ax, ay, bx, by):
    return math.sqrt((ax-bx)**2 + (ay-by)**2)


def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    # 메모이제이션
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)
    # 작은쪽으로 합병
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

N = int(input())
coord = [0] * N
distance = []
for i in range(0, N):
    x, y = map(float, input().split())
    coord[i] = [x, y, i+1]
check = [False] * N
# 일단 간선 가중치부터 구해놓아야한다.
# 이게 조합보다 훨씬 빠름!!! (why?조합은 재귀를 쓰므로, 오래걸린다..)

# 만약 nCr 에서 r이 정해진 상황이라면
# 조합 자체를 쓰기보다는 이렇게 for문 중첩으로 구현하자
for i in range(0, N-1):
    for j in range(i+1, N):
        edge_distance = calc_distance(coord[i][0], coord[i][1], coord[j][0], coord[j][1])
        distance.append([edge_distance, coord[i][2], coord[j][2]])


# 간선 가중치를 오름차순으로 정렬
distance.sort()
parent = [i for i in range(0, N+1)]

answer = 0
for i in range(0, len(distance)):
    cost, a, b = distance[i]

    # 아직 서로 부모노드가 안겹칠때만(아직 연결 안된것)g
        union(a, b)
        answer += cost
print(answer)
