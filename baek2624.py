import sys
sys.stdin = open("baek2624.txt")

"""
DP는 복습좀 하자..
DP[i][j] = DP[i][j] + DP[i-1][j-v*val] <- v를 1부터 p까지 반복
i번 동전까지 사용해서 j원을 만드는 경우  <= 이런 설계가 가능해야함

# 일반적인 수준의 DP 풀때 핵심,
위의 DP를 어떤 구조로 잡아야 할지 설계 할 수 있어야 한다.
+ 초깃값 설정, DP 탐색 로직 설계를 할 수 있어야 함

"""

T = int(input())
K = int(input())
coins = [0] *  K
for i in range(0, K):
    # 금액,  갯수
    p, n = map(int, input().split())
    coins[i] = (p, n)

DP = [[0] * (T+1) for _ in range(0, K+1)]
# 그냥 아예 안쓰는경우라고 생각하자. (일단 이런 초기화가 빡세네..)
DP[0][0] = 1

for i in range(1, K+1):
    amount, cnt = coins[i-1]
    # 0원부터 T원까지 순회 
    for j in range(0, T+1):
        # 직전값 전사
        DP[i][j] = DP[i-1][j] 
        for k in range(1, cnt+1):
            if j - k*amount >= 0:
                DP[i][j] += DP[i-1][j-k*amount]
            else:
                break
print(DP[K][T])