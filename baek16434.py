import sys
sys.stdin = open("baek16434.txt")

"""
이분탐색 모르겠고..
그냥 필요 HP 구하면 된다
몬스터 => 그 던전에서 소모되는 HP 구함 (체력//내 공격력)*(몬스터공격력)
포션 => 현재까지 소모된 체력 > 포션회복량이면 그대로반영
        아니면 무조건 0으로 (최소 HP구해야 되니까)
"""


N, H = map(int, sys.stdin.readline().split())
MAP = [0] * N
need = 0
attack = H
for i in range(0, N):
    t, a, b = list(map(int, sys.stdin.readline().split()))
    # 몬스터
    if t == 1:
        tmp = (b//attack)
        # 정확히 나누어 떨어지면 -1 해주어야함
        if (b % attack):
            need += tmp*a
        else:
            need += (tmp-1)*a

    # 포션
    else:
        # 공격력 증가
        attack += a
        # 현재까지 소모체력 > 포션 회복량이면 그대로 반영, 아니면 0으로
        if need > b:
            need -= b
        else:
            need = 0

print(need+1)
