import sys
sys.stdin = open("baek17406.txt")

def perm(arr, out, visited, depth, n, k):
    global answer

    if depth == k:
        temp = [[0] * M for _ in range(0, N)]
        min_val = INF
        for row in range(0, N):
            for col in range(0, M):
                temp[row][col] = MAP[row][col]

        for i in range(0, k):
            r, c, s = out[i]

            for j in range(1, s+1):
                # 윗변, r-s/c-s/r+s/c+s가 맵을 벗어나는 일은 없다
                # 상단
                tmp1 = temp[r-j][c+j]
                tmp2 = temp[r+j][c+j]
                tmp3 = temp[r+j][c-j] 
                for l in range(2*j-1, -1, -1):
                    temp[r-j][c-j+l+1] = temp[r-j][c-j+l]
                # 우측
                for l in range(2*j-1, 0, -1):
                    temp[r-j+l+1][c+j] = temp[r-j+l][c+j]
                temp[r-j+1][c+j] = tmp1
                # 하단
                for l in range(1, 2*j):
                    temp[r+j][c-j+l-1] = temp[r+j][c-j+l]
                temp[r+j][c+j-1] = tmp2

                # 좌측
                for l in range(1, 2*j):
                    temp[r-j+l-1][c-j] = temp[r-j+l][c-j]
                temp[r+j-1][c-j] = tmp3

        for row in range(0, N):
            tmp_sum = 0
            for col in range(0, M):
                tmp_sum += temp[row][col]
            min_val = min(tmp_sum, min_val)
        answer = min(answer, min_val)
        return
    for i in range(0, n):
        if visited[i]:
            continue
        visited[i] = True
        out[depth] = arr[i]
        perm(arr, out, visited, depth+1, n, k)
        visited[i] = False

N, M, K = list(map(int, input().split()))
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
opers = [0] * K
for i in range(0, K):
    a, b, s = list(map(int, input().split()))
    opers[i] = [a-1, b-1, s]

visited = [False] * K
out = [0] * K
INF = 987654321
answer = INF
perm(opers, out, visited, 0, K, K)
print(answer)