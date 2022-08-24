import sys
sys.stdin = open("baek1260.txt")

"""
DFS 는 스택으로
BFS 는 큐로 진행

DFS가 재귀로도 가능한것은, 메모리 자체가 스택구조로 처리되기 때문!

얘 그리고 양방향
"""



class Stack:
    def __init__(self, capacity):
        self.max = capacity
        self.stk = [0] * self.max
        self.data = 0
        self.ptr = 0
    
    def push(self, x):
        if self.data >= self.max:
            raise IndexError
        self.stk[self.ptr] = x
        self.data += 1
        self.ptr += 1
        return x

    def pop(self):
        if self.data <= 0:
            raise IndexError
        self.ptr -= 1
        now = self.stk[self.ptr]
        self.data -= 1
        return now

    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.stk[self.ptr-1]

    def isEmpty(self):
        return self.data <= 0


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
    
    def isEmpty(self):
        return self.data <= 0


# DFS는 더이상 방문할 수 없는 경우일때 pop을 하는 형태!
def dfs(n, v, graph):
    res = []
    stk = Stack(n*n)
    stk.push(v)
    visited = [False] * (n+1)
    visited[v] = True

    while not stk.isEmpty():
        now = stk.peek()
        if now not in res:
            res.append(now)
        tmp = []
        for node in graph[now]:
            if visited[node]:
                continue
            tmp.append(node)
        if tmp:
            tmp.sort()
            # 갈 수 있는 경로중 node값이 가장 낮은 곳
            next = tmp[0]
            visited[next] = True
            stk.push(next)
        # 갈수 없을때 pop을한다
        else:
            stk.pop()
    return res


def bfs(n, v, graph):
    res = []
    que = Queue(n*n)
    que.enqueue(v)
    visited = [False] * (n+1)
    visited[v] = True
    while not que.isEmpty():
        now = que.dequeue()
        res.append(now)
        tmp = []
        for node in graph[now]:
            if visited[node]:
                continue
            visited[node] = True
            tmp.append(node)
        tmp.sort()
        for i in range(0, len(tmp)):
            que.enqueue(tmp[i])
    return res


N, M, V = map(int, input().split())
Graph = [[] * (N+1) for _ in range(N+1)]
for i in range(0, M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)
answer1 = dfs(N, V, Graph)
answer2 = bfs(N, V, Graph)
for i in range(0, len(answer1)):
    if i == len(answer1) - 1:
        print(answer1[i])
    else:
        print(answer1[i], end=" ")
for i in range(0, len(answer2)):
    if i == len(answer2) - 1:
        print(answer2[i])
    else:
        print(answer2[i], end=" ")