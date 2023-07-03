import sys
sys.stdin = open("baek2346.txt")


N = int(input())
nums = list(map(int, input().split()))


visited = [False] * N
visited[0] = True
cnt = 1
ans = [1]
node = 0

while cnt < N:
    path = nums[node]
    next_node = node
    if path > 0:
        while path > 0:
            next_node += 1
            if next_node >= N:
                next_node = 0       
            if not visited[next_node]:
                path -= 1
    else:
        while path < 0:
            next_node -= 1
            if next_node < 0:
                next_node = N-1
            if not visited[next_node]:
                path += 1
    cnt += 1
    visited[next_node] = True
    ans.append(next_node+1)
    node = next_node

print(" ".join(map(str, ans)))