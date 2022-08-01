"""
비트마스킹

&& 둘다 1이어야만1, 따라서 한쪽이 0이면 0으로 됨
|| 둘다 0이어야만 0 따라서 한쪽이 1이면 1로됨 (주로 비트 추가할때 사용)
^ (Xor) 서로 다른 비트면 1 같은 비트면 0이됨
>> 한자리 작은 위치로 이동  (십진수 기준 *(1/2))
<< 한자리 큰 위치로 이동    (십진수  기준  *2)

이문제 반드시 따로 답지 안보고 풀어볼 것
"""



N = int(input())
mod = 1000000000
# DP[a][b][c]  a는 비트 정보 (1부터 2**11-1 즉 1023까지, 1 부터 111111111 까지 사용)
# b는 자릿수  c는 끝나는 수 현재 뽑은 수에서 마지막 자리 
# ex. 만약 내가 345654 라는 수를 뽑았다면 f(비트정보)는 0001111000 b는 6 c는 4가 되는것
DP = [[[-1] * 11 for _ in range(0, N+1)] for _ in range(1 << 11)]


def go(f, b, x):

    # N자리 수를 다 뽑은 상황일 때 (종료 조건)
    if b == N:
        # 2**0  부터 2**9까지가 전부 뽑힌것 111111111 (1023) 
        # 즉 2의 n 자리가 의미하는것이 해당 계단수에서 n이란 값을 사용했다는 의미!
        if f == (1 << 10) -1:
            # f가 111111111 때만 정답
            return 1
        return 0
    # 초깃값이 아닌경우에는 해당 값을 반환

    if DP[f][b][x] != -1:
        return DP[f][b][x]
    # DP[f][b][x] == -1이면 (초기상황) 일단 0으로 시작
    DP[f][b][x] = 0
    # 끝나는자리가 0이면 1 큰 값만 올 수 있음, 0 ~ 9만 사용 가능하므로 + 계단수
    if x == 0:
        # 현재 f 비트 정보에다가 내가 현재 쓴 비트를 추가할때 | 사용!
        # ex 현재 0000000001 인 경우 즉 1만 쓴 경우에서 2를 추가로 사용하였으므로
        # 000000001  
        # 000000010 이 두 비트를 | 를 하면 000000011 즉 0과 1을 사용했다는 비트 정보를 담을 수 있다!
        DP[f][b][x] += go(f | (1 << (x+1)), b+1, x+1)
        DP[f][b][x] %= mod
    # 끝나는 자리가 9면 1 작은값만 올 수 있음, 0 ~ 9만 사용 가능하므로 + 계단수
    elif x == 9:
        DP[f][b][x] += go(f | (1 << (x-1)), b+1, x-1)
        DP[f][b][x] %= mod
    # 1 ~ 8 사이라면 1 큰 값, 1 작은값 둘다 가능
    else:
        DP[f][b][x] += go(f | (1 << (x+1)), b+1, x+1)
        DP[f][b][x] %= mod
        DP[f][b][x] += go(f | (1 << (x-1)), b+1, x-1)
        DP[f][b][x] %= mod
    return DP[f][b][x]

ans = 0


# 가장 큰 숫자가 1 ~ 9인 경우 각각 체크
for i in range(1, 10):
    # 가장 큰 자릿수가 i 인 경우
    ans += go(1 << i, 1, i)
    ans %= mod
print(ans)