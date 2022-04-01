import sys
sys.stdin = open("baek9095.txt")

"""
최대 값이 10이므로,
BFS or DFS // 
둘다 풀린다. => 문제 조건보고 이런걸 파악 할 수 있어야한다.
범위 값이 보통
10 이하 => DFS로도 어떻게든 가능
100 이하 => DFS 가지치기하면 가능
이보다 범위가 크면 보통 DFS로는 힘들다.
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


def bfs(num):
    count = 0
    que = Queue(1000)
    # 1부터 3까지 저장
    for i in range(1, 4):
        que.enqueue(i)

    while not que.isEmpty():
        now = que.dequeue()
        # 종료 조건
        if now == num:
            count += 1
            continue
        for i in range(1, 4):
            next = now + i
            if next > num:
                continue
            que.enqueue(next)
    return count

def dfs(now, goal):
    global count
    if now == goal:
        count += 1
        return
    for i in range(1, 4):
        next = now + i
        if next > goal:
            continue
        dfs(next, goal)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    dfs(0, N)
    print(count)
    # ans = bfs(N)
    # print(ans)