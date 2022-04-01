import sys
sys.stdin = open("baek9461.txt")
"""
첫 5행은 정해줘야하고,
그 이후부터는
P(N) = P(N-1) + P(N-5) 점화식이다!

DP 는  일반적으로 아래 크게 2가지로 진행된다.
메모이제이션 => 레알 점화식 (피보나치, 파도반수열)
이전의 저장된 값과 현재 비교하려는 값 중 최솟값을 비교 or T/F 여부를 체크하며 DP 진행 (집 색칠하기,기타리스트 ...)
"""


# n은 1부터 따라서 인덱스랑 1차이가 난다.
def pado(n):
    if n <= 5:
        return DP[n-1]

    # n == i-1
    for i in range(6, n+1):
        DP.append(DP[i-2] + DP[i-6])
    return DP[n-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 처음에 5개는 있어야한다.
    DP = [1, 1, 1, 2, 2]
    ans = pado(N)
    print(ans)


