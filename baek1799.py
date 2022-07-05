import sys
sys.stdin = open("baek1799.txt")

"""
전략1. 그냥 DFS로.?

우상향 대각선은 x+y = i    => 0 ~ 2N까지
우하향 대각선은 x-y = i임

이걸 N퀸 문제처럼 푸는것!

N퀸문제랑 이거랑 다시 풀어보자!

집에가서 재귀 공부 다시하자!
"""


# 현재 대각선 번호에서부터 추가할 수 있는 대각선의 최대 갯수
def upper_bound(arr, diag, n):
    cnt = 0
    for d in range(diag, 2*n-1):
        for y in range(0, d+1):
            x = d-y
            if 0 <= x < n and 0 <= y < n and arr[y][x] and rd[x-y] == 0:
                # 갯수만 세는것
                cnt += 1
                break
    return cnt

def bishop(arr, diag, count, n):
    global max_count

    # 종료조건
    if diag == 2*n:
        max_count = max(count, max_count)
        return

    ub = upper_bound(arr, diag, n)
    # 앞으로 더 두어봤자 현재까지의 최댓값보다 작을 경우는 더 볼 필요 X
    if ub + count <= max_count:
        return
    # y가 row x가 col
    for y in range(0, diag+1):
        x = diag-y  # x+y = diag (대각선 번호) , 우하향 대각선까지 체크
        if 0 <= x < n and 0 <= y < n and arr[y][x] and rd[x-y] == 0:
            rd[x-y] = 1
            bishop(arr, diag+1, count+1, n)
            rd[x-y] = 0
   
    bishop(arr, diag+1, count, n)
        

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

rd = {} # 우하향 대각선 맨 왼쪽아래가 -N+1, 맨 오른쪽위가 N-1
for i in range(-N+1, N):
    rd[i] = 0 #초기화

max_count = 0
bishop(MAP, 0, 0, N)
print(max_count)