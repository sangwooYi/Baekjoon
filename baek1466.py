import sys
sys.stdin = open("baek1466.txt")


"""
그냥 DP 문제다..
DP 문제도 다시 풀어보자
"""
N, D = map(int, input().split())
DP = [i for i in range(0, D+1)]

short_cuts = [0] * N

for i in range(0, N):
    s, e, cost = map(int, input().split())
    
    short_cuts[i] = (s, e, cost)

# 0부터 D까지 쭉 순회
for i in range(0, D+1):
    # DP[i-1] 에서 그냥 왔을떄와 DP[i] 까지 현재 저장값중 최솟값을
    # 매번 갱신
    if i > 0:
        DP[i] = min(DP[i], DP[i-1]+1)

    for s, e, cost in short_cuts:
        if e > D:
            continue
        if s == i:
            DP[e] = min(DP[e], DP[i]+cost)
print(DP[D])