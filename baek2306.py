import sys
sys.stdin = open("baek2306.txt")

"""
at / gc 가 가장 기본 KOI
X 가 KOI 일때,  aXt , gXc 도 KOI
X, Y가 KOI면 XY도 KOI
ex) aatatgct 얘도 KOI인것 (aXXYt) 니까 
포인트는 t가 나올때 이전에 남아있는 a가 있는지 / c가 나올때 남아있는 g 가있는지?

DP[a][b] a ~ b, 까지 KOI 최대 길이

문제 그대로 풀었으면 되었을 문제! 너무 어렵게 생각하지말자..
다시 풀어 볼 것

DP 에서 중요한것은, 동적 판단으로 인해, 언뜻보면 의미없어 보이는 순회도 그냥 진행해도 된다는것!

"""


DNA = list(input())
N = len(DNA)
DP = [[0] * (N+1) for _ in range(0, N+1)]


# 길이 1 부터 ~ N-1까지 순회
for size in range(1, N):
    for start in range(0, N-size):
        # start, end 범위가 0~1에서부터  N-2 ~ N-1 까지 범위를 전부 체크해보는것임
        end = start + size 
        # X가 KOI면 aXt, gXc도 KOI, 여기서 그냥 at, gc인 경우까지 체크가 됨 (이땐 X, Y가 공집합인 셈)
        if (DNA[start] == "a" and DNA[end] == "t") or (DNA[start] == "g" and DNA[end] == "c"):
            DP[start][end] = DP[start+1][end-1] + 2 
        
        # X, Y 가 KOI면 XY도 KOI다 현재 start~end 값 vs start~mid / mid+1 ~ end 까지중 더 긴길이를
        # 매번 확인하여 갱신한다.
        for mid in range(start, end):
            DP[start][end] = max(DP[start][end], DP[start][mid] + DP[mid+1][end])

print(DP[0][N-1])
