import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek1949.txt")

"""
1. 우수 마을로 선정된 주민 합이 최대가 되야함
2. 우수마을은 인접하면 안됨
3. 우수마을이 아닌 마을은 최소한 하나 이상의 우수마을과 인접

트리에서 DP 하는거 연습..

DP[n][1] 은 n번 마을을 우수마을로 선택할때의 총 합
DP[n][0] 은 n번 마을을 우수마을로 선택하지 않았을 때의 총합

따라서 
DP[now][1] += DP[인접노드][0] 
현재 노드를 선택한 경우에는, 인접 노드는 반드시 선택하면 안되므로!

DP[now][0] += max(DP[인접노드][0], DP[인접노드][1])
만약 선택 안하는 경우에는 인접노드를 선택할 때, 안할 때중 더 큰 값을 넣어주면 된다

이렇게 점화식을 세울 수 있어야 한다!

DP는 결국 메모이제이션 / 점화식을 얼마나 잘 세우냐의 싸움ㅠㅠ

이렇게 DFS + DP 같이 쓰는 문제도 혼자 풀수 있어야한다.
+ 재귀에 대해 더 확실히 이해할 필요가 있음
"""

def dfs(now):
    # 현재 노드 방문 체크
    visited[now] = True
    for next_node in graph[now]:
        # 방문 체크 안된 노드라면
        if not visited[next_node]:
            # 재귀 진행 (스택 진행은 아래처럼 진행 된다.)
            """
            우선 아래 순서대로 stack에 push 됨
            1 -> 2        마지막으로 얘가 pop 
            2 -> 3
                 3 -> 4
                 4 -> 5    여기부터 스택 pop

            2 -> 6
                 6 -> 7   위에 2->3 끝나면 이제 여기가 pop

            """
            dfs(next_node)
            # 선택한 경우와 안선택한 경우를 나누어서 체크
            DP[now][1] += DP[next_node][0]
            DP[now][0] += max(DP[next_node][0], DP[next_node][1])


N = int(input())
# 파이썬서는 그냥 리스트 끼리 합산이 가능 (가변 리스트이기 때문)
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(0, N+1)]
parent = [i for i in range(0, N+1)]
visited = [False] * (N+1)

DP = [[0, populations[i]] for i in range(0, N+1)]

for i in range(0, N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(DP[1][1], DP[1][0]))
