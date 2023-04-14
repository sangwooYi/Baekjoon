import sys
sys.stdin = open("baek21940.txt")


INF = 987654321
N, M = map(int, input().split())

dist = [[INF] * (N+1) for _ in range(0, N+1)]
for i in range(0, M):
    a, b, t = map(int, input().split())
    # 일방통행
    dist[a][b] = t

C = int(input())
friends_pos = list(map(int, input().split()))

for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                dist[s][e] = 0
            dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])


check_dict = {}
for i in range(1, N+1):
    now_max = 0
    for j in range(0, C):
        tmp = 0
        pos = friends_pos[j]
        tmp += dist[pos][i]
        tmp += dist[i][pos]
        now_max = max(now_max, tmp)
    if now_max not in check_dict.keys():
        check_dict[now_max] = [i]
    else:
        check_dict[now_max].append(i)

answer_key = list(check_dict.keys())
answer_key.sort()

answer = check_dict[answer_key[0]]
answer.sort()
print(" ".join(map(str, answer)))