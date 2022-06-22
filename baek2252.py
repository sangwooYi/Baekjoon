import sys
sys.stdin = open("baek2252.txt")

"""
위상정렬
: 그래프에서 '순서'를 명확히 지켜야 하는 경우
사용할 수 있는 방법!
=> 엄격한 순서가 전체적으로 정해지지는 않는다
순서가 정해져 있는 노드들에 대해서만 순서가 정해질 뿐!
(엄격하게 조건을 주지 않는이상, 여러가지 경우의 수가 나올 수 밖에 없음)

1. 방향성 그래프상태로 저장하면서 진입차수 체크 
2. 진입차수 0인 애들이 시작점이 된다, que에 enqueue
3. BFS를 진행하며, 아래와같이 진행
    1) 현재 체크하는 노드에서 갈 수 있는 방향을 전부 체크
    2) 갈 수 있는 다음 노드가 있다면 그 다음노드의 진입차수를 1 감소 시킴
    3) 만약 진입차수가 0이되었다면, 이제 그 노드로 넘어가도 된다는 것 
       필요한 작업 체크하고 그 다음노드를 que에 enqueue함

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
in_degree = [0] * (N+1)
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 해당 노드로 들어오는 차수가 증가
    in_degree[b] += 1

result = [0] * N
idx = 0


que = Queue(100*N)

for i in range(1, N+1):
    if in_degree[i] == 0:
        result[idx] = i
        idx += 1
        que.enqueue(i)

while not que.is_empty():
    node = que.dequeue()
    for next_node in graph[node]:
        in_degree[next_node] -= 1

        if in_degree[next_node] == 0:
            result[idx] = next_node
            idx += 1
            que.enqueue(next_node)

print(" ".join(map(str, result)))