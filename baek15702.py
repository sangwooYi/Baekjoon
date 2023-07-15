import sys
sys.stdin = open("baek15702.txt")

N, M = map(int, input().split())

scores = list(map(int, input().split()))
arr = [0] * M
for i in range(0, M):
    tmp = list(input().split())
    num = int(tmp[0])
    cur_res = tmp[1:]
    score = 0
    for j in range(0, N):
        if cur_res[j] == "O":
            score += scores[j]
    arr[i] = [num, score]
arr.sort(key=lambda x : [-x[1], x[0]])

print(f"{arr[0][0]} {arr[0][1]}")