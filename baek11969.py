import sys
sys.stdin = open("baek11969.txt")


N, Q = map(int, sys.stdin.readline().split())

arr = [[0] * 4 for _ in range(0, N+1)]

for i in range(1, N+1):
    id = int(sys.stdin.readline().rstrip())
    arr[i][id] += 1

sum_arr = [[0] * 4 for _ in range(0, N+1)]

for i in range(1, N+1):
    for j in range(1, 4):
        sum_arr[i][j] = sum_arr[i-1][j] + arr[i][j]

for i in range(0, Q):
    a, b = map(int, sys.stdin.readline().split())

    cur = [0] * 4
    
    for j in range(1, 4):
        cur[j] += sum_arr[b][j]

        if a > 1:
            cur[j] -= sum_arr[a-1][j]


    print(" ".join(map(str, cur[1:])))