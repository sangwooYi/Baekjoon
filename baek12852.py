
N = int(input())
DP = [0] * (N+1)
path = [[] for _ in range(0, N+1)]
for i in range(N-1, 0, -1):
    # 등호 ㅡㅡ
    if 3*i <= N:
        min_val = min(DP[3*i], DP[2*i], DP[i+1])
        DP[i] = min_val+1
        if DP[3*i] == min_val:
            path[i] = 3*i
        elif DP[2*i] == min_val:
            path[i] = 2*i
        else:
            path[i] = i+1
    elif 2*i <= N:
        min_val = min(DP[2*i], DP[i+1])
        DP[i] = min_val+1
        if DP[2*i] == min_val:
            path[i] = 2*i
        else:
            path[i] = i+1
    else:
        DP[i] = DP[i+1] + 1
        path[i] = i+1
print(DP[1])
ans = "1"
idx = 1
while True:
    if path[idx]:
        ans = str(path[idx]) + " " + ans
        idx = path[idx]
    else:
        break
print(ans)
