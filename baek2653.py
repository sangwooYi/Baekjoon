import sys
sys.stdin = open("baek2653.txt")



N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

stable = True
for i in range(0, N-1):
    for j in range(i+1, N):
        # 만약 서로가 연결이 다르면 애초에 불안정한집단인것
        if MAP[i][j] != MAP[j][i]:
            stable = False
            break
    if not stable:
        break

visited = [False] * N
group = []
cnt = 0
for i in range(0, N):
    if visited[i]:
        continue
    visited[i] = True
    cnt += 1
    group.append([i+1])
    for j in range(0, N):
        if i == j:
            continue
        # 일단 연결되어있으면 스택에 추가
        if MAP[i][j] == 0:
            group[cnt-1].append(j+1)
            visited[j] = True
# 그룹이 1개라면 본인 자신밖에 없는것 따라서 pass
for i in range(0, len(group)):
    if len(group[i]) < 2:
        stable = False
        break
if stable:
    print(cnt)
    for i in range(0, len(group)):
        print(" ".join(map(str, group[i])))
else:
    print(0)