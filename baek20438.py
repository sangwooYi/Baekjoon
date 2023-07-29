import sys
sys.stdin = open("baek20438.txt")


N, K, Q, M = map(int, input().split())
sleeps = list(map(int, input().split()))
attendances = list(map(int, input().split()))

# 3번부터 N+2번까지 번호를 받는다
sleep_map = {}
for sleep in sleeps:
    sleep_map[sleep] = 1

arr = [1] * (N+3)

for attendance in attendances:

    if attendance not in sleep_map.keys():
        arr[attendance] = 0

        num = 2
        cur = attendance*num
        while cur < N+3:
            if cur not in sleep_map.keys():
                arr[cur] = 0
            num += 1
            cur = attendance*num


sum_arr = [0] * (N+3)
sum_arr[3] = arr[3]

for i in range(4, N+3):
    sum_arr[i] = sum_arr[i-1]+arr[i]


for i in range(0, M):
    left, right = map(int, sys.stdin.readline().split())
    ans = sum_arr[right]
    if left > 3:
        ans -= sum_arr[left-1]
    print(ans)