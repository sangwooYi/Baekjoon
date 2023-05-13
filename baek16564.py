import sys
sys.stdin = open("baek16564.txt")


"""
이건 upper bound
lower bound / upper bound / 단순 이분탐색 구분

연산횟수 최대 백만 * 30(2**30) 

목표레벨 T 를 가정하고 전부 T 이상으로 맞춘다.
=> 이때 필요한 레벨 체크
1) K보다 크면 줄여야 함
2) K보다 작거나 같으면 늘린다. (upper bound) 

최초 시작
pl = 1
pr = (10억+10억+1)
"""

def upper_bound():
    pl = 1
    pr = 2000000001

    while pl < pr:
        # 목표 팀레벨
        pc = (pl+pr)//2
        req_lev = 0
        
        for cur_lev in characters:

            if pc > cur_lev:
                req_lev += (pc-cur_lev)
        
        if req_lev > K:
            pr = pc
        else:
            pl = pc+1
    # upper bound는 특성상 최대범위+1에서 끝난다!
    return pl-1

N, K = map(int, sys.stdin.readline().split())
characters = [0] * N
for i in range(0, N):
    characters[i] = int(input())

ans = upper_bound()
print(ans)