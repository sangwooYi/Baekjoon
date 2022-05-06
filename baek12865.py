import sys
sys.stdin = open("baek12865.txt")

"""
요거 DP 대표  문제임!
DP 유형은 꼭 기억해두자
"""

N, K = map(int, input().split())
items = [0] * N
for i in range(0, N):
    items[i] = list(map(int, input().split()))

# DP[a] 무게가 a인 상황에서 최대의 가치
DP = [0] * (K+1)
for i in range(0, len(items)):
    w, v = items[i]
    for j in range(K, w-1, -1):
        #  이런걸 혼자 생각할 수 있어야 한다 ㅠ
        DP[j] = max(DP[j], DP[j-w]+v)

print(DP[-1])


