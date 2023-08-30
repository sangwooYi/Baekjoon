import sys
sys.stdin = open("baek2799.txt")


answer = [0] * 5
N, M = map(int, input().split())

row_cnt = 5*N+1
col_cnt = 5*M+1

MAP = [0] * row_cnt


for i in range(0, row_cnt):
    MAP[i] = list(input())

for i in range(0, N):
    for j in range(0, M):
        flag = True
        for k in range(0, 4):
            if MAP[5*i+1+k][5*j+1] == ".":
                answer[k] += 1
                flag = False
                break
        if flag:
            answer[4] += 1

print(" ".join(map(str, answer)))
