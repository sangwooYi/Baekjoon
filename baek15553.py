import sys
sys.stdin = open("baek15553.txt")


N, K = map(int, input().split())
visit_times = [0] * N
for i in range(0, N):
    visit_times[i] = int(input())

term_list = [0] * (N-1)

for i in range(1, N):
    term_list[i-1] = visit_times[i]-visit_times[i-1]-1

term_list.sort()

add_time = 0
req_add_cnt = 0
if N > K:
    req_add_cnt = N-K

for i in range(0, req_add_cnt):
    add_time += term_list[i]
print(N+add_time)