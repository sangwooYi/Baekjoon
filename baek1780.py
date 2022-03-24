import sys
sys.stdin = open("baek1780.txt")

"""
분할정복을 사용해야하는 문제!

길이가 1이 될때까지 분할
도중에 모든 값이 같은수면 중단 후 count
=> 길이가 1이 된경우에도 해당 숫자 count
"""

def dfs(pl, pr, pu, pd):
    # 길이가 1인것 (종료조건1)
    if pl == pr or pu==pd:
        ans[MAP[pu][pl]+1] += 1
        return
    flag = True
    start = MAP[pu][pl]
    # pu ~ pd // pl ~ pr 까지 탐색해야한다. range(a, b) a 부터 b-1까지 탐색하는것 주의!
    for row in range(pu, pd+1):
        if not flag:
            break
        for col in range(pl, pr+1):
            if MAP[row][col] != start:
                
                flag = False
                break
    # 모두 같은 수인것 (종료조건2)
    if flag:
        ans[start+1] += 1
        return
    term = (pr-pl+1) // 3
    # 1분면
    dfs(pl, pl+term-1, pu, pu+term-1)
    # 2분면
    dfs(pl+term, pl+(term*2)-1, pu, pu+term-1)
    # 3분면
    dfs(pl+(term*2), pr, pu, pu+term-1)
    # 4분면
    dfs(pl, pl+term-1, pu+term, pu+(term*2)-1)
    # 5분면
    dfs(pl+term, pl+(term*2)-1, pu+term, pu+(term*2)-1)
    # 6분면
    dfs(pl+(term*2), pr, pu+term, pu+(term*2)-1)
    # 7분면
    dfs(pl, pl+term-1, pu+(term*2), pd)
    # 8분면
    dfs(pl+term, pl+(term*2)-1, pu+(term*2), pd)
    # 9분면
    dfs(pl+(term*2), pr, pu+(term*2), pd)

N = int(input())
MAP = [0] * N
for i in range(0, N):
    temp = list(map(int, input().split()))
    MAP[i] = temp
ans = [0] * 3
dfs(0, N-1, 0, N-1)
for i in range(0, 3):
    print(ans[i])