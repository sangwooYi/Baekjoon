import sys
import math
sys.stdin = open("baek16434.txt")

"""
아래처럼 O(N)으로 풀수도 있는 문제
10억번 연산이 거의 1초정도라 생각하면 편함
"""


N, H = map(int, sys.stdin.readline().split())


maxHP, curlHP, damage = 0, 0, 0
attack = H

for i in range(0, N):
    t, a, b = list(map(int, sys.stdin.readline().split()))
    # 몬스터
    if t == 1:
        tmp = (b//attack)
        # 정확히 나누어 떨어지면 -1 해주어야함
        if (b % attack):
            damage = -tmp*a
        else:
            damage = -(tmp-1)*a

    # 포션
    else:
        # 공격력 증가
        attack += a
        damage = b
    # 매 턴 끝날때마다 damage를 계산해 주는것
    curlHP += damage
    # 포션 회복량이 초과 된 경우
    if curlHP > 0:
        curlHP = 0
    # 여기서 체크하는구만, 포션 먹기전까지 누적 데미지 // 현재까지 계산된 maxHP중 큰 값 선택 
    maxHP = max(maxHP, abs(curlHP))

print(maxHP+1)


# 정석으로 푸는건 이분탐색이다. 참고
N, att = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

# left는 최소hp right는 최대 hp 
# 이분탐색의 범위가 용사 HP인 문제
"""
이문제가 이분탐색으로 풀리는 원리

우리가 원하는 최소의 HP값을 찾기 위해

최소 1   최대 INF 값을 잡아 이분탐색을 진행하는것

=> 스무고개를 한다고 생각하면 된다.
현재 범위에서의 중간값을 찍어서
=> HP가 부족한지, 남는지를 판단

남는다면 => 더 작은 값이어야함 (최대를 줄여야함 최댓값이 현재 중간값-1)
부족하다면 => 더 큰 값이어야함 (최솟값이 현재 중간값+1)

이걸 통해 우리가 원하는 답이 나올때까지 계속 이분탐색을 진행하는것

(2**30) == 10억

즉 10억정도 범위의 어떠한 자연수라도 31번 안에 때려맞출 수 있다.

이 포인트를 살린 문제이다
"""
left = 1
right = 10000000000000000
answer = 0
# 이 조건 끝날떄까지 계속 반복함
while left <= right:
    mid = (left+right)//2
    hp, attack = mid, att
    
    for i in range(0, N):
        t, a, h = MAP[i]
        if t == 1:
            # math.ceil 올림 math.floor 내림 math.round 반올림
            hp -= (math.ceil(h / attack)-1) * a
            # hp 가 0이된다면 우리가 원하는 답은 더 커야 한다.
            if hp <= 0:
                break
        else:
            attack += a
            # 이 문제에서의 핵심은 포션을 먹는 단계
            hp = min(mid, hp+h)
    # hp가 남는 경우면 최댓값을 줄인다.
    if hp > 0:
        right = mid-1
        answer = mid
    # hp가 0이하가 되었다면 부족한 경우, 따라서 최소hp를 오히려 늘려야 한다.
    else:
        left = mid+1

print(answer)
