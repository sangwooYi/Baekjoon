import sys
sys.stdin = open("baek23978.txt")


def sum_one_to_num(num):
    return (num)*(num+1)//2

def sum_a_to_b(num_a, num_b):
    return sum_one_to_num(num_b)-sum_one_to_num(num_a)+num_a

N, K = map(int, input().split())
days = list(map(int, input().split()))

left = 1
# right를 왜 이렇게 잡았는지가 포인트..
# 가장 최소금액으로 얻을 수 있는경우는 N 이 1일때이므로
# K <= (X*(X+1)//2) => 이때 X 값이 약 15억정도로 나옴!
right = 1500000000

while left < right:
    mid = (left+right)//2
    total_cash = 0
    for i in range(0, N-1):
        term = days[i+1]-days[i]-1
        if term >= mid:
            term = mid-1
        total_cash += sum_a_to_b(mid-term, mid)
    total_cash += sum_one_to_num(mid)
    if total_cash >= K:
        right = mid
    else:
        left = mid+1
print(left)
