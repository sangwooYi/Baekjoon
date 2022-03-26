import sys
sys.stdin = open("baek1495.txt")

"""
i 번째 노래를 연주하기 위해서는
P + V[i] 혹은 P - V[i] 로 볼륨을 변경해야하고,
볼륨은 0 이상, M 이하여야한다.
이 범위를 벗어나면 다음 곡 연주가 불가능 (-1 반환)

방법
D[i] = D[i-1] + V[i]가 기본
근데 만약 이게 M 을 벗어나면
D[i] = D[i-2] - V[i-1] + V[i] 가 될것이다.
근데 D[i-2] - V[i-1] < 0 이면 변경 불가능인것
"""

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
DP = [0] * (N+2)
for i in range(1, N+1):
    pass
