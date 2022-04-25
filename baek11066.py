import sys
sys.stdin = open("baek11066.txt")

"""
이문제 개빡쏀데ㅡㅡ?
그냥 나중에 한번 다시 풀어볼것

table[i][j] 는 i 부터 j 까지의 최소합
여기서 포인트는
table[i][j] = table[i][j-1] + pages[j] + min(table[i][k] + table[k+1][j])

지금까지 푼 DP 방식과 좀 다르다! 이런 방식도 혼자서 풀 수 있어야함!
기본적으로 재귀를 사용하지 않고 구현한다고 생각하자!
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pages = list(map(int, input().split()))

    # 그냥 단순히 i 부터 j 요소까지의 합만 저장해 두는 작업
    table = [[0] * N for _ in range(0, N)]
    for i in range(0, N-1):
        table[i][i+1] = pages[i] + pages[i+1]
        for j in range(i+2, N):
            table[i][j] = table[i][j-1] + pages[j]
    
    # 이부분이 핵심이다!    
    # 재귀로 안돌리고, i ~ j 까지의 최소합을 분할하여 구한 방식
    # ex) d = 2, N = 6이라면
    # i = 0 1 2 3  
    # j = 2 3 4 5 이렇게 부분합을 체크할 수 있는것!
    # 이렇게 d를 N-1까지 확장, d 가 N-1이란건 그냥 전체 범위라는것!
    for d in range(2, N):
        for i in range(N-d):    
            j = i+d
            # 부분합 구하는 부분
            temp_sum = []
            for k in range(i, j):
                temp_sum.append(table[i][k] + table[k+1][j])
            table[i][j] += min(temp_sum)
    print(table[0][N-1])