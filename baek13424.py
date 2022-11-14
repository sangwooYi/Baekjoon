import sys

sys.stdin = open("baek13424.txt")


T = int(input())
for tc in range(0, T):
    N, M = map(int, input().split())
    INF = 987654321
    dist = [[INF] * (N+1) for _ in range(0, N+1)]

    for i in range(0, M):
        a, b, c = map(int, input().split())
        # 양방향, 같은 노드 쌍에 대한 중복 데이터 X (문제 잘 읽기!)
        dist[a][b] = c
        dist[b][a] = c
    K = int(input())
    friends = list(map(int, input().split()))

    # 플로이드 와샬 헷갈리지 말자! 반복문에서 w (간선)이 가장 먼저 온다.
    for w in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                if start == end:
                    dist[start][end] = 0
                else:
                    dist[start][end] = min(dist[start][end], dist[start][w] + dist[w][end])
    
    answer = -1
    min_sum = INF
    for room in range(N, 0, -1):
        tmp_sum = 0
        for friend in friends:
            tmp_sum += dist[friend][room]
        if tmp_sum <= min_sum:
            min_sum = tmp_sum
            answer = room
    print(answer)