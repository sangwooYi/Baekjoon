import sys
sys.stdin = open("baek11659.txt")

"""
이런건 포기하지말고 좀만더 생각해보자...
누적합 배열을 통해 풀 수 있는 문제!
arr = [0, a, a+b, a+b+c, a+b+c+d ...]
이런식일때
3 ~ 5번째 구간합을 구하고 싶으면
arr[5] - arr[2] 을 하면된다!
(a+b+c+d+e) - (a+b)
"""


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
acc_arr = [0] * (N+1)
sum = 0
# 누적 구간합 배열 생성
for i in range(0, N):
    sum += nums[i]
    acc_arr[i+1] = sum
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    print(acc_arr[b]-acc_arr[a-1])