import sys
sys.stdin = open("baek1082.txt")

"""
1. 자릿수가 최대한 커야함
2. 그 안에서, 앞자리가 최대한 높은 숫자여야 함

다시 풀어 볼 것
기본적으로 DP를 푸는 개념을 머릿속에 박아두자!

= 메모이제이션
= 점화식
점화식을 잘 세울 수 있어야 한다!
"""

N = int(input())
nums = list(map(int, input().split()))
M = int(input())


# M원을 통해 만들 수 있는 최대 방크기가 저장
DP = [0] * (M+1)
# 가능한 앞자리가 높은 숫자여야함, 따라서 N-1부터 0 까지 순회
# 이러면 자연스레 0이 제일 먼저 나오는경우는 알아서 제껴짐!
for i in range(N-1, -1, -1):
    # 가격
    x = nums[i]
    for j in range(x, M+1):
        # 큰 수부터 순회하므로, 이전에 구매한 애는 일단 최대한 큰 수일 것이다!
        # 따라서 DP[j-x]*10 에서 +i 를 더해주는것
        # DP[j-x]*10 + i 와 현재 DP[j] 중 큰 값을 매번 체크한다!
        DP[j] = max(DP[j-x]*10+i, DP[j])
print(DP[M])

