import sys
sys.stdin = open("baek2579.txt")

"""
그리디!
아이디어1
거꾸로 시작.
도착 -> 0번인덱스까지진행하며
그다음 , 그다다음중 큰값을 선택하면서 끝까지 진행
연속갯수가 3개가 안넘도록 체크

DP 는 기본적으로 점화식 세우기!
DP 문제는 앞으로 좀만 더 생각해보자
N = 1일때에도, DP[3] 까지 계산해야하므로 N+3 길이를 선언한것!
"""


N = int(input())
DP = [0] * (N+3)
stairs = [0] * (N+3)

for i in range(1, N+1):
    stairs[i] = int(input())
    DP[1] = stairs[1]
    DP[2] = stairs[1] + stairs[2]
    DP[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for k in range(4, N+1):
        DP[k] = max(DP[k-3] + stairs[k-1] + stairs[k], DP[k-2] + stairs[k])
print(DP[N]) 