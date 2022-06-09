import sys
import decimal
sys.stdin = open("baek4781.txt")

"""
주어진 가격에 100을 곱해서,
정수로 만든 다음에 이걸로 체크하자

그냥 배낭 문제임!

최대가격 >= 현재 가격인 경우에
DP[i] = max(DP[i], DP[i-p]+c)
를 하면 되는 문제
그래봤자 p는 10000까지임, 최솟값은 1

그냥 Float() 을 쓰게되면 부동소숫점 오차가 발생한다!
따라서. 
ㅅ
"""

while True:
    N, M = input().split()
    N = int(N)
    if N == 0:
        break
    M = int(decimal.Decimal(M) * 100)
    candies = [0] * N
    for i in range(0, N):
        c, p = input().split()
        candies[i] = int(c), int(decimal.Decimal(p) * 100)
    DP = [0] * (M+1)

    for i in range(1, M+1):
        for j in range(0, N):
            v, w = candies[j]
            # 현재 따지려는 값 이하인 가격의 경우에만
            if i >= w:
                DP[i] = max(DP[i], DP[i-w]+v)

    print(max(DP))