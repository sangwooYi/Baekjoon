import sys
sys.stdin = open("baek18428.txt")


def comb(arr, start, visited, n, r, k):
    global flag
    # 하나라도 성공하면 끝
    if flag:
        return
    if k == 0:
        tmp = [0] * r
        idx = 0
        for i in range(0, n):
            if visited[i]:
                tmp[idx] = arr[i]
                idx += 1
        # 3개를 놓을 수 있는 경우.
        for i in range(0, r):
            row, col = tmp[i]
            MAP[row][col] = "O"
        is_block = True
        for teacher in teachers:
            if not is_block:
                break
            row, col = teacher
            for d in range(0, 4):
                if not is_block:
                    break
                a = 1
                next_row = row + dr[d]*a
                next_col = col + dc[d]*a
                while 0 <= next_row < N and 0 <= next_col < N:
                    if MAP[next_row][next_col] == "S":
                        is_block = False
                        break
                    # 장애물
                    if MAP[next_row][next_col] == "O":
                        break
                    a += 1
                    next_row = row + dr[d]*a
                    next_col = col + dc[d]*a
        if is_block:
            flag = True
        # 원복
        for i in range(0, r):
            row, col = tmp[i]
            MAP[row][col] = "X"
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, i+1, visited, n, r, k-1)
        visited[i] = False

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input().split())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
flag = False
teachers = []
blanks = []
for r in range(0, N):
    for c in range(0, N):
        if MAP[r][c] == "T":
            teachers.append((r, c))
        elif MAP[r][c] == "X":
            blanks.append((r, c))
visited = [False] * len(blanks)
comb(blanks, 0, visited, len(blanks), 3, 3)

if flag:
    print("YES")
else:
    print("NO")