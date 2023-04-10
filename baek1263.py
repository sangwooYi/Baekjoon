import sys
sys.stdin = open("baek1263.txt")


N = int(input())
schedules = [0] * N
for i in range(0, N):
    t, s = map(int, input().split())
    schedules[i] = (t, s)

schedules.sort(key=lambda x : -x[1])

answer = schedules[0][1] - schedules[0][0]

for i in range(1, N):
    req_time, time_limit = schedules[i]

    if time_limit < answer:
        answer = time_limit-req_time
    else:
        answer -= req_time
if answer < 0:
    answer = -1
print(answer)