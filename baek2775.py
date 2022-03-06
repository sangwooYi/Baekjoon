"""
k층 n호의 인원수 => k-1층 1호부터 n호까지의 합! 즉 거꾸로 계속 재귀를 보내야 한다

DP 없이 재귀로만 // DP 사용 (후자가 가능하면 후자가 훨씬 좋음)
전자도 성공하네 ㅡㅡ?
0.5 초 => 0.016초 ㄷㄷ
# DP로하면 시간이 말도안되게 단축 됨
"""

import sys
sys.stdin = open("baek2775.txt")


# DP 기본문제! DP도 사용 가능해야한다.
def find_num(k, n):
    if k == 0:
        return n
    # 아직 DP에 저장 안된경우는 재귀 돌려 계산해야함
    if DP[k][n-1] == 0:
        sum = 0
        for i in range(1, n+1):
            sum += find_num(k-1, i)
        DP[k][n-1] = sum    
    # 값이 있는경우는 바로 그 값을 반환 (n층은 1층부터 ~ 14층까지이므로
    #  인덱스로는 0 ~ 13까지 헷갈리면 더미 데이터 놓는 방식을 쓸것)
    return DP[k][n-1]


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    N = int(input())
    # 15행 14열이어야 한다.
    DP = [[0] * 14 for _ in range(0, 15)]
    # 초깃값 세팅
    for i in range(0, 14):
        DP[0][i] = i + 1
    answer = find_num(K, N)
    print(answer)