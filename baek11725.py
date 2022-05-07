import sys
sys.stdin = open("baek11725.txt")
sys.setrecursionlimit(10**6)
"""
1이 루트인것이고, 그 외에는 차례대로 따라 내려가야한다!
dfs 쓸꺼면 sys.setrecursionlimit(10**6) 미리 걸어두고 시작하자
BFS, DFS 둘다 가능한 풀이
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

# DFS 풀이
def dfs(node):
    for next_node in graph[node]:
        if parent[next_node]:
            continue
        parent[next_node] = node
        dfs(next_node)

N = int(input())
parent = [0] * (N+1)
graph = [[] for _ in range(0, N+1)]
for i in range(2, N+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
for i in range(2, len(parent)):
    print(parent[i])

# BFS 풀이
# que = Queue(20*N)
# que.enqueue(1)
# visited[1] = True
# while not que.is_empty():
#     node = que.dequeue()
#     for next_node in graph[node]:
#         if parent[next_node]:
#             continue
#         parent[next_node] = node
#         que.enqueue(next_node)
# for i in range(2, len(parent)):
#     print(parent[i])