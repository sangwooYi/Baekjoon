import sys
sys.stdin = open("baek14465.txt")


# N 총 갯수, K 원하는 연속수, B 고장난 수
N, K, B = map(int, sys.stdin.readline().split())
arr = [1] * (N+1)
arr[0] = 0
for i in range(0, B):
    n = int(sys.stdin.readline().rstrip())
    arr[n] = 0

sum_arr = [0] * (N+1)
for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

min_num = 987654321

for i in range(1, N+2-K):
    cur_num = sum_arr[i+K-1]
    if i > 1:
        cur_num -= sum_arr[i-1]
    
    cur_sub = K-cur_num
    min_num = min(min_num, cur_sub)
print(min_num)