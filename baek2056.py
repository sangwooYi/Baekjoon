import sys
sys.stdin = open("baek2056.txt")

"""
1005번과 완전 동일한 문제!

'최소'라는 말에 속지 말자.

순서가 정해져있으므로

1
   3  
2
에서 3번 완료 할 수 있는 가장 빠른 시간은 
결국 1 -> 3   /  2 - > 3 과정중
오래 걸린 시간이 된다!
(결국 1, 2 전부 끝날 떄 까지 기달려야 하므로)
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
        self.front += 1
        self.data -= 1
        if self.front == self.max:
            self.front = 0
        return now
    
    def is_empty(self):
        return self.data <= 0

    def size(self):
        return self.data


N = int(input())
in_order = [0] * (N+1)
require_times = [0] * (N+1)
graph = [[] for _ in range(0, N+1)]
for i in range(0, N):
    tmp = list(map(int, input().split()))
    require_times[i+1] = tmp[0]
    # 선행관계에 있는 작업 수들
    post_num = tmp[1]
    for j in range(0, post_num):
        in_order[i+1] += 1
        graph[tmp[j+2]].append(i+1)

DP = [0] * (N+1)
que = Queue(100000)
for i in range(1, N+1):
    if in_order[i] == 0:
        DP[i] += require_times[i]
        que.enqueue(i)


while not que.is_empty():
    node = que.dequeue()
    for next_node in graph[node]:
        in_order[next_node] -= 1
        DP[next_node] = max(DP[next_node], DP[node] + require_times[next_node])

        if in_order[next_node] == 0:
            que.enqueue(next_node)
# 반드시 N번째가 마지막 차례가 아닐 수 있다. 
# 예를들어 N, N-1, N-2 번쨰가 동시에 마지막 차례일수도있는것 
# 따라서 DP[N] 이 아닌 max(DP) 로
print(max(DP))