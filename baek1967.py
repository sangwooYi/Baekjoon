import sys
sys.stdin = open("baek1967.txt")

"""
일반 그래프에서는, 가중치가 존재하면
단순 BFS를 하면 안된다, (경로는 길지만 더 적은 비용이 존재할 수 있으므로)
하지만 트리에서는 항상 노드간 간선은 1개
따라서 가중치 있어도 BFS 가능
"""

class Queue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0
    
    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def is_empty(self):
        return self.data <= 0




def bfs(graph, n):
    que = Queue(20*n)
    visited = [False] * (N+1)
    # 일단 아무노드에서 출발 (난 1번노드)
    visited[1] = True
    que.enqueue((1, 0))
    max_path = 0
    max_node = 0
    while not que.is_empty():
        node, path = que.dequeue()
        if max_path < path:
            max_path = path
            max_node = node
        for next_node, next_path in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            total_path = path + next_path
            que.enqueue((next_node, total_path))
    
    # 한번 더
    visited = [False] * (N+1)
    visited[max_node] = True
    que.enqueue((max_node, 0))
    result = 0
    while not que.is_empty():
        node, path = que.dequeue()
        if result < path:
            result = path
        for next_node, next_path in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            total_path = path + next_path
            que.enqueue((next_node, total_path))
    return result
    


N = int(sys.stdin.readline())
G = [[] for _ in range(0, N+1)]
# 간선은 N-1개 존재
for i in range(0, N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    # 대신 무방향
    G[a].append((b, c))
    G[b].append((a, c))
answer = bfs(G, N)
print(answer)