from collections import deque


A, B, N, M = map(int, input().split())

def plus_one(num):
    return num+1

def minus_one(num):
    return num-1

def plus_A(num):
    return num+A

def minus_A(num):
    return num-A

def plus_B(num):
    return num+B

def minus_B(num):
    return num-B

def kake_A(num):
    return num*A

def kake_B(num):
    return num*B

def bfs():
    visited = [False] * 100001
    operators = [plus_one, minus_one, plus_A, minus_A, plus_B, minus_B, kake_A, kake_B]

    que = deque()
    que.append((N, 0))
    visited[N] = True

    while que:
        node, cnt = que.popleft()

        if node == M:
            return cnt
        
        for i in range(0, 8):
            cur_func = operators[i]

            next_node = cur_func(node)

            if next_node < 0 or next_node > 100000:
                continue
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append((next_node, cnt+1))

answer = bfs()
print(answer)

