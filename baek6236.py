import sys
sys.stdin = open("baek6236.txt")

"""
lower bound : 원하는 값이 나올 때 다음 탐색값을 줄인다. 
upper bound : 원하는 값이 나올 때 다음 탐색값을 키운다.
그냥 이분 탐색: 원하는 값이 나오는것만 관심이 있다.

lower bound 문제.

mid 값이 인출할 돈 K 값
해당 인출값으로 진행할 때 
K 번보다 적거나 같게 인출 => K 값을 줄인다
K 번보다 많게 인출 => K 값을 키운다
"""

N, M = map(int, input().split())
spendings = [0] * N
max_spending = 0
for i in range(0, N):
    spendings[i] = int(input())
    max_spending = max(max_spending, spendings[i])
# 최소한 그날 지출할 금액만큼은 인출해야한다.
pl = max_spending
# 최대는 10만일동안 1만원씩 인출 즉 10만*1만 (10억)
pr = 1000000001

while pl < pr:
    pc = (pl+pr)//2

    # 무조건 한번은 인출하고 시작
    withdraw_cnt = 0
    change_amount = 0
    for spending in spendings:

        if change_amount >= spending:
            change_amount -= spending
        else:
            withdraw_cnt += 1
            change_amount = (pc-spending)
    if withdraw_cnt <= M:
        pr = pc
    else:
        pl = pc+1

print(pl)