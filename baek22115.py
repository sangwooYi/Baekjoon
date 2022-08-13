import sys
sys.stdin = open("baek22115.txt")

"""
DP[i][j]
i 번째까지, j만큼의 카페인을 섭취하기위해 필요한 커피의 수


"""


N, K = map(int, input().split())
coffees = list(map(int, input().split()))
INF = 999999999
if K == 0:
    # 무조건 0
    ans = 0
else:
    DP = [[INF] * (K+1) for _ in range(0, N+1)]

    flag = True
    for i in range(0, N):
        caffeine = coffees[i]
        if caffeine == K:
            # 한개로만 만들수 있는경우 체크
            ans = 1
            flag = False
            break
        if caffeine <= K:
            DP[i+1][caffeine] = 1
    # 한개로만 만들수 없는 경우
    if flag:
        for i in range(0, N):
            caffeine = coffees[i]
            for j in range(1, K+1):
                # 만약 이전 애까지에서 j값을 만들수있는 이전 경우가 있었으면 전사해줌
                if DP[i][j] != INF:
                    DP[i+1][j] = min(DP[i][j], DP[i+1][j])
                # 그다음 배낭 문제 진행
                if caffeine <= j:
                    DP[i+1][j] = min(DP[i+1][j], DP[i][j-caffeine] + 1)
        ans = DP[N][K]

if ans == INF:
    print(-1)
else:
    print(ans)