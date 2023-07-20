import sys
sys.stdin = open("baek1032.txt")

N = int(input())

arr = [0] * N
for i in range(0, N):
    arr[i] = list(input())
# 파일 길이는 모두 같다
visited = [True] * len(arr[0])

for i in range(1, N):
    for j in range(0, len(arr[0])):
        if arr[0][j] != arr[i][j]:
            visited[j] = False
            
ans = ""
for i in range(0, len(arr[0])):
    if visited[i]:
        ans += arr[0][i]
    else:
        ans += "?"
print(ans)