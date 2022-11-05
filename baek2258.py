import sys
sys.stdin = open("baek2258.txt")


"""
같은 가격이 여러개 존재할수도있음!

포인트는 현재 고른 고기값보다 싼 고기들은 공짜로 준다는것
+ 해당 가격의 고기를 다 살 필요는 없다..

가격은 저렴한순으로, 같은가격이라면 높은 양을 주는 순으로 정렬
+ 현재 금액 단위의 고기로 만약에 필요양을 맞출 수 있으면?
=> 일단 현재 금액단위에서 가능한 최소금액 체크.
이걸 높은단위로 올라가며 계속 반복 + 그 이전금액까지의 총량을 누적으로 가지고 감
이 과정에서 최소 비용을 계속 갱신해 나감
"""

N, M = map(int, sys.stdin.readline().split())
meets = [0] * N
for i in range(0, N):
    amount, cost = map(int, sys.stdin.readline().split())
    meets[i] = (amount, cost)

# 금액은 오름차순, 같은 금액끼리는 양은 내림차순
meets.sort(key=lambda x : (x[1], -x[0]))


current_cost = 0 
total_cost = 0
total_amount = 0
INF = 999999999999
result = INF
flag = False
for i in range(0, N):
    amount, cost = meets[i]
    if i == 0:
        current_cost = cost
        total_cost = cost
    else:
        if current_cost == cost:
            if not flag:
                total_cost += cost
        # cost > current_cost
        else:
            total_cost = cost
            current_cost = cost
    total_amount += amount
    if total_amount >= M:
        flag = True
        result = min(result, total_cost)
if result == INF:
    result= -1
print(result)

