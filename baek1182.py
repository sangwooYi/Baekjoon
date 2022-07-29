import sys
sys.stdin = open("baek1182.txt")

"""
연속되지 않은 경우도 부분 수열이라고 본다!
"""

def comb(arr, visited, start, n, r):
    global answer 

    if r == 0:
        temp = 0
        for i in range(0, len(arr)):
            if visited[i]:
                temp += arr[i]
        if temp == S:
            answer += 1
        return
    for i in range(start, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, visited, i+1, n, r-1)
        visited[i] = False



N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(1, N+1):
    check = [False] * N
    comb(nums, check, 0, N, i)
print(answer)