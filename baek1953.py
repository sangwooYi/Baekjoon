import sys
sys.stdin = open("baek1953.txt")
from collections import deque


def bfs(start_node):
    
    visited[start_node] = True
    que = deque()
    
    start_team = NO_TEAM
    for next_node in graph[start_node]:
        if team_arr[next_node] == NO_TEAM:
            continue
        if team_arr[next_node] == BLUE:
            start_team = WHITE
        else:
            start_team = BLUE
        break
    if start_team == NO_TEAM:
        start_team = BLUE
    que.append((start_node, start_team))

    while que:
        node, team = que.popleft()
        
        if team == BLUE:
            blue_team.append(node)
            next_team = WHITE
        else:
            white_team.append(node)
            next_team = BLUE

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append((next_node, next_team))

NO_TEAM = 0
BLUE = 1
WHITE = 2
N = int(input())
check_dict = {}
graph = [[] for _ in range(0, N+1)]
visited = [False] * (N+1)
team_arr = [NO_TEAM] * (N+1)
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    cnt = tmp[0]
    haters = tmp[1:]
    
    for hater in haters:
        left_node = min(i, hater)
        right_node = max(i, hater)

        if (left_node, right_node) not in check_dict.keys():
            graph[i].append(hater)
            graph[hater].append(i)
            check_dict[(left_node, right_node)] = 1

blue_team = []
white_team = []

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
blue_team.sort()
white_team.sort()
print(len(blue_team))
print(" ".join(map(str, blue_team)))
print(len(white_team))
print(" ".join(map(str, white_team)))