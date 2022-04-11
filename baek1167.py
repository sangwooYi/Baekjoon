import sys
sys.stdin = open("baek1167.txt")

"""
기본적으로 단방향 그래프인듯?
정점갯수가 10만개까지. 완전탐색은 택도없다
최악의 경우 한 노드에 대한 탐색 수가 10만 x 10먄 

트리의 지름!
트리일때만 가능,
임의의 노드에서, 가장 최댓값을 갖는 노드 선정,
그 노드에서부터 최대거리를 구하면 그게 답이된다!

이 문제는 한번 더풀어보자

https://blog.myungwoo.kr/112

"""
class Queue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.front = 0
        self.rear = 0
        self.data = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear == 0
        return x

    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.rear == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


def bfs(graph, v):
    que = Queue(10000000)
    visited = [-1] * (v+1)
    que.enqueue(1)
    visited[1] = 0

    max_path = 0
    max_node = 0
    while not que.is_empty():
        node = que.dequeue()
        # 트리이기떄문에 모든 노드를 결국 방문은 하게된다.
        for next_node, next_path in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + next_path
                que.enqueue((next_node))
                if max_path < visited[next_node]:
                    max_node = next_node
                    max_path = visited[next_node]

    # 위 bfs에서 특정 노드에서 최대거리를 갖는 노드를 체크, 그 노드에서부터 최대의 거리를 갖는 길이를 찾는다.
    visited = [-1] * (v+1)
    que.enqueue(max_node)
    max_path = 0
    visited[max_node] = 0
    while not que.is_empty():
        node = que.dequeue()
        for next_node, next_path in graph[node]:
            if visited[next_node]  == -1:
                visited[next_node] = visited[node] + next_path
                que.enqueue((next_node))
                if max_path < visited[next_node]:
                    max_path = visited[next_node]
    return max_path


V = int(sys.stdin.readline())
G = [[] for _ in range(0, V+1)]
for i in range(0, V):
    temp = list(map(int, sys.stdin.readline().split()))
    node = temp[0]
    # len(temp) - 3까지만 탐색
    for j in range(1, len(temp)-2, 2):
        G[node].append((temp[j], temp[j+1]))

ans = bfs(G, V)
print(ans)