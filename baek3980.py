import sys
sys.stdin = open("baek3980.txt")


# 순열로 가야함
def perm(arr, visited, depth, n, total):
    global answer

    if depth == n:
        answer = max(answer, total)
        return

    for i in range(0, n):
        if visited[i]:
            continue
        # 수치 0이면 아예 참가 못함 (문제 잘 읽자)
        if arr[depth][i] == 0:
            continue
        now_score = arr[depth][i]
        if total+now_score+(n-depth-1)*100 < answer:
            continue
        next_total = total+now_score
        visited[i] = True
        perm(arr, visited, depth+1, n, next_total)
        visited[i] = False

T = int(input())
num = 11
for tc in range(0, T):
    players = [0] * num
    for i in range(0, num):
        players[i] = list(map(int, input().split()))

    visited = [False] * num

    answer = 0
    perm(players, visited, 0, num, 0)
    print(answer)