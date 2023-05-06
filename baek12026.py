import sys
sys.stdin = open("baek12026.txt")


"""
DP[a][b]
a번 까지 b번 문자열까지 만들었을때 에너지 최소량
B=0 , O=1, J=2 이고 다서 J=2 => B=0 으로 간다!

2606번이랑 유사한 문제!
"""
INF = 987654321
N = int(input())
CHARS = list(input())

DP = [[INF]*3 for _ in range(0, N)]
# 초깃값 설정, 첫번째글자는 무조건 B
DP[0][0] = 0
PAT = ["B", "O", "J"]


for j in range(1, N):
    for k in range(0, j):
        for i in range(0, 3):
            if CHARS[j] == PAT[i]:
                pre_idx = (i-1+3)%3
                DP[j][i] = min(DP[j][i], DP[k][pre_idx]+(j-k)**2)

ans = min(DP[N-1])
if ans == INF:
    ans = -1
print(ans)