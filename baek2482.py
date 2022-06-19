import sys
sys.stdin = open("baek2482.txt")

"""
DP[i][j] 
=> i개 색상중 j개를 선택하 경우라는 의미

이런 점화식을 세울 수 잇어야한다. 
만약 j번째를 선택한다면 i-1번째선택 못하므로, 
i-2개 색상중 j-1개를 뽑은거에서 j번선택
DP[i-2][j-1]
안선택한다면 DP[i-1][j] 인것 
DP[i][j] = DP[i-2][j-1] + DP[i-1][j]

근데 만약 i가 n이라면=> 첫번쨰도 고려해줘야한다.
따라서 N번째 선택한다면, 1번 N-1번 두개를 못쓰게 됨. 
따라서 Dp[i-3][K-1] + DP[i-1][K]
(N개중의 K개 선택할때 따져준다.)

다시 풀어 볼 것

+ 나머지정리
(a*b)%mod = ((a%mod) * (b%mod))%mod
"""

N = int(input())
K = int(input())
mod = 1000000003

DP = [[0] * (K+1) for _ in range(0, N+1)]

#  DP 초기화
for i in range(0, N+1):
    # i개 중 아예 선택 안하는것은 1가지밖에없음
    DP[i][0] = 1
    # i 개중 1개 선택하는 방법은 i가지
    DP[i][1] = i

for i in range(2, N+1):
    for j in range(2, K+1):
        DP[i][j] = (DP[i-2][j-1] + DP[i-1][j]) % mod


# N개중의 K 개선택할때는 N번째일경우를 별도로 체크 
DP[N][K] = (DP[N-3][K-1] + DP[N-1][K]) % mod
print(DP[N][K])