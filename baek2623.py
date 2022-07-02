import sys
sys.stdin = open("baek2623.txt")

"""
전형적인 위상정렬 문제

1. 진입차수를 체크
2. 진입차수가 0인애부터 시작 (큐에 엔큐)
=> 기본적으로는 BFS이며
현재 노드 => 도착노드를 순회하며 도착노드의 진입차수를 -1
도착노드의 진입차수가 0이면 그때 큐에 저장

이 문제처럼 위상정렬이 불가능한 경우도 있음!
(정렬이 중간에 끊겨버림) why? 만약 
1 4 3
6 2 5 4
3 2 
이렇게 된다면  
1 4 3 2  과  6 2 5 4 가 충돌한다! (이런경우 
위상정렬 로직이 중간에 끊기는것)
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


N, M = map(int, input().split())
graph = [[] for _ in range(0, N+1)]

in_order = [0] * (N+1)
for i in range(0, M):
    temp = list(map(int, input().split()))
    nodes = temp[1:]
    for j in range(0, len(nodes)-1):
        graph[nodes[j]].append(nodes[j+1])
        in_order[nodes[j+1]] += 1

order = [0] * N
idx = 0

que = Queue(N*200)
for i in range(1, N+1):
    if in_order[i] == 0:
        que.enqueue(i)
        order[idx] = i
        idx+=1
    
while not que.is_empty():
    node = que.dequeue()

    for next_node in graph[node]:
        in_order[next_node] -= 1
        if in_order[next_node] == 0:
            order[idx] = next_node
            idx += 1
            que.enqueue(next_node)

flag = False
for i in range(0, N):
    if order[i] == 0:
        flag = True
        break
if flag:
    print(0)
else:
    for i in range(0, N):
        print(order[i])