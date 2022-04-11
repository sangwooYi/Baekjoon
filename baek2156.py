import sys
sys.stdin = open("baek2156.txt")

"""
아이디어1.
max(D[n-2] + n, D[n-3] + n-1 + n, D[n-4]+n-1+n)
이걸 계속 누적해나가는것 
여기에 두잔연속 안마시는 경우도 포함!
반레도 생각할 수 있어야한다.
"""



N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = int(input())
DP = [0] * N
if N == 1:
    print(MAP[0])
elif N == 2:
    print(MAP[0] + MAP[1])
else:
    DP[0] = MAP[0]
    DP[1] = MAP[0] + MAP[1]
    DP[2] = max(MAP[0]+MAP[2], MAP[1]+MAP[2])
    for i in range(3, N):
        if i >= 4:
            DP[i] = max(DP[i-4]+MAP[i-1]+MAP[i], DP[i-3]+MAP[i-1]+MAP[i], DP[i-2]+MAP[i])
        else:
            DP[i] = max(DP[i-3]+MAP[i-1]+MAP[i], DP[i-2]+MAP[i])
    ans = 0
    for i in range(0, len(DP)):
        if ans < DP[i]:
            ans = DP[i]
    print(ans)