import sys
sys.stdin = open("baek21318.txt")


N = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().split()))


sum_arr = [0] * N
for i in range(1, N):
    if scores[i-1] > scores[i]:
        sum_arr[i] = sum_arr[i-1]+1
    else:
        sum_arr[i] = sum_arr[i-1]


Q = int(sys.stdin.readline().rstrip())
for i in range(0, Q):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1
    e -= 1
    
    ans = sum_arr[e]
    if s > 0:
        ans -= sum_arr[s]
    print(ans)