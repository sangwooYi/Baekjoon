import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek17265.txt")


def dfs(now_val, row, col, oper):
    global min_val
    global max_val


    for d in range(0, 2):
        next_row = row + dr[d]
        next_col = col + dc[d]
        
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue
        next_val = MAP[next_row][next_col]
        if next_val in operators:
            next_total = now_val
            next_oper = next_val
        else:
            next_val = int(next_val)
            next_oper = ""
            if oper == "+":
                next_total = now_val + next_val
            elif oper == "-":
                next_total = now_val - next_val
            else:
                next_total = now_val * next_val
            
            if next_row == N-1 and next_col == N-1:
                min_val = min(min_val, next_total)
                max_val = max(max_val, next_total)
                continue
        dfs(next_total, next_row, next_col, next_oper)
        

# 우, 하
dr = [1, 0]
dc = [0, 1]
operators = ["+", "-", "*"]
N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input().split())

# 최솟값이 0이 아닐 수 있다! 실수하지말자..
min_val = 987654321
max_val = -987654321
start_num = int(MAP[0][0])
visited = [[False] * N for _ in range(0, N)]
visited[0][0] = True
dfs(start_num, 0, 0, "")

print(f"{max_val} {min_val}")