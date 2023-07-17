import sys
sys.stdin = open("baek10025.txt")

"""
복잡도 O(N) 
2백만회
"""


N, K = map(int, input().split())

upper_limit = 1000001
# 0 ~ 100만까지
orders = [0] * upper_limit
sum_arr = [0] * upper_limit

for i in range(0, N):
    g, x = map(int, input().split())
    orders[x] = g


sum_arr[0] = orders[0]
for i in range(1, upper_limit):
    sum_arr[i] = sum_arr[i-1]+orders[i]


max_amount = 0

for i in range(0, upper_limit):

    left = i-K
    right = i+K

    if left < 0:
        left = 0
    if right >= upper_limit:
        # 1,000,000이 최고
        right = upper_limit-1
    
    cur_amount = sum_arr[right]
    if left > 0:
        cur_amount -= sum_arr[left-1]
    max_amount = max(max_amount, cur_amount)
print(max_amount)