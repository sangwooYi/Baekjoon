import sys
sys.stdin = open("baek13702.txt")


"""
mid 만큼 나누어줄때 
K 보다 적게 나오면
=> mid 를 줄인다.

K 보다 크거나 같게나오면 mid를 늘린다.

upper bound

최대 수치는 2**31 - 1 (약 20억)
"""



N, K = map(int, input().split())
arr = [0] * N
for i in range(0, N):
    arr[i] = int(input())


left = 1
right = 2**31

while left < right:
    mid = (left+right)//2

    cur = 0
    for i in range(0, N):
        # 남는건 버린다, 따라서 정수로 나누어떨어지는 만큼만 분배
        cur += (arr[i]//mid)

    if cur < K:
        right = mid
    else:
        left = mid+1
print(left-1)