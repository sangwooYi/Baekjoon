import sys
sys.stdin = open("baek1389.txt")

"""
기본적으로 그래프문제에서는
양방향인지 단방향인지부터 체크!
(서로 친구이므로 양방향)
N은 최대 100까지
a -> b 노드로 갈때 최소 경로를 구하는것
BFS
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
    
    def isEmpty(self):
        return self.data <= 0


# a -> b노드 까지의 최소 경로 값을 return
def kevinBacon(a, b, graph):
    que = Queue(N*N)
    # 노드수가 1부터 N 까지 
    visited = [False] * (N+1)
    que.enqueue((a, 0))
    visited[a] = True
    while not que.isEmpty():
        now = que.dequeue()
        now_node = now[0]
        path = now[1]
        for next_node in Graph[now_node]:
            if visited[next_node]:
                continue
            # 갈 수 있는 곳
            if next_node == b:
                return (path + 1)
            visited[next_node] = True
            que.enqueue((next_node, path+1))



N, M = map(int, input().split())
# 빈 리스트 선언이므로 아래와같이만해도된다. 빈 리스트를 (N+1) 행만큼 생성하는것
# 굳이 [] * (N+1) 안해줘도 됨!
Graph = [[]  for _ in range(0, N+1)]
for i in range(0, M):
    A, B = map(int, input().split())
    Graph[A].append(B)
    Graph[B].append(A)
answer = [0] * (N+1)
for i in range(1, N+1):
    sum = 0
    for j in range(1, N+1):
        if j == i:
            continue
        tmp = kevinBacon(i, j, Graph)
        sum += tmp
    answer[i] = sum
# 같은 경우에는 작은 인덱스값을 출력하기 위해, 현재기준보다 작은 경우 에만 갱신!
ans_node = 1
min_count = answer[1]
for i in range(2, N+1):
    if min_count > answer[i]:
        min_count = answer[i]
        ans_node = i
print(ans_node)
