import sys
sys.stdin = open("baek21921.txt")


N, X = map(int, sys.stdin.readline().split())
visiters = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * N
sum_arr[0] = visiters[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1]+visiters[i]

if sum_arr[N-1] == 0:
    print("SAD")
else:
    cnt = 0
    max_visiters = 0
    for i in range(0, N-X+1):
        start_idx = i
        end_idx = i+X-1
        
        cur_visiters = sum_arr[end_idx]
        if start_idx > 0:
            cur_visiters -= sum_arr[start_idx-1]
        if cur_visiters > max_visiters:
            cnt = 1
            max_visiters = cur_visiters
        elif cur_visiters == max_visiters:
            cnt += 1
    print(max_visiters)
    print(cnt)