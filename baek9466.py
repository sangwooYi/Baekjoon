import sys
sys.setrecursionlimit(110000)
sys.stdin = open("baek9466.txt")


"""
재귀에 대해 이해할 필요가 있다.
다시 풀어볼 것.
"""


def dfs(now):
    global result
    visited[now] = True
    cycle.append(now)
    vote = nums[now]

    # 더이상 dfs 진행 불가
    if visited[vote]:
        # 현재 투표한애가 사이클안에 있으면
        if vote in cycle:
            # 사이클 발생하는 구간만 더해주기 (파이썬 인덱싱 잘 활용할 수 있어야 한다.)
            result += cycle[cycle.index(vote):]
        return
    else:
        # dfs 진행
        dfs(vote)


T = int(sys.stdin.readline())
for tc in range(0, T):
    N = int(sys.stdin.readline())
    nums = [-1] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if nums[i] == i:
            visited[i] = True
            cnt += 1

    if cnt < N:
        result = []
        for i in range(1, N+1):
            if not visited[i]:
                cycle = []
                dfs(i)
        cnt += len(result)
    print(N-cnt) 