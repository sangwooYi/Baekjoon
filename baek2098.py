import sys
sys.stdin = open("baek2098.txt")

"""
외판원 순회 (Traveling Salesman Problem, TSP)

포인트는 DP + 비트마스킹이란것
비트마스킹은 방문한 노드를 저장하기 위해 사용
ex) 총 노드가 4개일때, 4자리 비트를 사용 (1<<4 - 1) 
여기서 1101 이면 1, 2, 4번째 노드를 방문한것 -> 이런식으로 방문 노드를 체크
DP[a][b] 현재 이미 들른 도시 정보가 b이고 (비트 정보), 현재 있는도시가 a일때
아직 방문 안한 나머지 도시들을 방문한 뒤 출발 도시로 돌아오는 최소 비용
총 노드가 4개이고 만약 b가 1001 , a = 4라면, 현재 1,4번만 방문한 상태이며 여기서 2,3 번을 
추가로 방문한 경로에서 최소비용을 담는 공간이 되는 것

점화식은 아래와 같이 나온다
DP[i][j] = min(DP[i][j], DP[i][j | (1 << k)] + DP[i][k])
=> 1011 에서 만약 3번 노드를 방문한 걸 체크하고 싶으면
1011 | 1 << 2 를 해주면 된다, 그럼 1111이 됨  (1011 | 0100 의 or 비트 연산은 1111)
=> 이런게 비트마스킹!
&, |, ^, 전부 활용 가능해야함 (^, XOR 는 서로 다른 비트인 경우만 1이 되는 것)

여기서 포인트는 결국 출발점으로 돌아오기 때문에 사이클(Cycle)이 형성 됨
따라서, 출발 노드를 어디로 잡아도 결국 같은 결과가 나옴!        

반드시 다시 풀어 볼것
재귀에 대해서 확실히 이해해야 한다! 
"""

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))


INF = 987654321
DP = [[0] * (1 << N) for _ in range(0, N)]

# 어차피 출발지가 어디든 상관 없으니 1번을 출발지로 정한다.
def dfs(now, visited):
    # 이미 방문한 경로면 바로 return
    if DP[now][visited]:
        return DP[now][visited]
    # 모든 노드를 전부 방문한 경우 (ex 노드가 4이면 1111)
    if visited == (1 << N) - 1:
        if MAP[now][0]:
            return MAP[now][0]
        else:
            return INF
    
    cost = INF
    # 2번 노드부터 N번 노드까지 전부 순회
    for i in range(1, N):
        # 경로가 없으면 (0인 경우) pass
        if not MAP[now][i]:
            continue
        # 이미 방문한 경우 pass (ex 1100에서 이미 3번 노드를 방문했으므로 i가 2일떄 (3번노드 체크) continue가 됨)
        if visited & (1 << i):
            continue
        # 현재 비용을 체크 (이 부분을 재귀로 진행 DFS도 연습하자..)
        cost = min(cost, dfs(i, visited | (1 << i)) + MAP[now][i])
    # 메모이제이션
    DP[now][visited] = cost 
    # 최종 계산된 결과가 반환 된다.
    return DP[now][visited]
# 1번에서 부터 출발(1번 노드이지만 인덱스와 1차이)
answer = dfs(0, 1)
print(answer)
