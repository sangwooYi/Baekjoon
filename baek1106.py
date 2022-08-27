import sys
sys.stdin = open("baek1106.txt")

"""
DP 문제 중
배낭 문제는, 배낭문제임을 파악할 수 있어야 한다.

주로.
가치와, cost 들이 주어질 때
특정 가치를 만들기 위해 최소한의 cost를 구하는 문제
혹은 특정 cost에서 만들 수 있는 최대한의 가치를 구하는 문제들이 주로 나온다.

여기서는
적어도 C의 고객을 얻기위해 투자해야하는 최소한의 금액
=> 정확히 C 명이아님. 주의!

조금만 더 생각해보자.. 이것도 혼자 충분히 풀 수 있었는데..
"""

C, N = map(int, input().split())
infos = [0] * N


INF = 987654321
DP = [INF] * (C+101)
# 이렇게 초깃값 설정이 중요하다..
DP[0] = 0
for i in range(0, N):
    # cost(비용), 얻는 고객 수(가치)
    cost, value = map(int, input().split())
    infos[i] = [cost, value]

for i in range(0, N):
    cost, value = infos[i]
    for j in range(value, C+101):
        DP[j] =  min(DP[j-value]+cost, DP[j])
answer = DP[C]
for i in range(C+1, C+101):
    answer = min(answer, DP[i])
print(answer)
