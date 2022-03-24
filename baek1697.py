import sys
sys.stdin = open("baek1697.txt")
"""
진짜 그냥 일일이 계산 ㅡㅡ?
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


def min_time(n, k):
    que = Queue(1000000)
    que.enqueue((n, 0))
    while True:
        now = que.dequeue()
        num = now[0]
        path = now[1]
        if num > 100000:
            continue
        if DP[num] <= path:
            continue
        DP[num] = path
        if num == k:
            return DP[k]
        if num >= 1:
            que.enqueue((num-1, path+1))
        if num < 100000:
            que.enqueue((num+1, path+1))
        if num*2 <= 100000:
            que.enqueue((num*2, path+1))
    

N, K = map(int, input().split())
INF = 99999
DP = [INF] * 100001
if N <= K:
    ans = min_time(N, K)
# 이경우에는 거꾸로 가는 방법밖에 없다!
else:
    ans = (N-K)
print(ans)

# def bfs(a, b):
#     if b < 0 or b > 100000:
#         return
#     # 아직 방문 안했거나, 이동되서 온 값이 현재 저장값보다 작을 떄
#     if (visit[b] == 0) or (visit[a]+1 < visit[b]):
#         visit[b] = visit[a] + 1
#         que.enqueue(b)

# N, K = map(int, input().split())
# INF = 99999
# visit = [0] * 100001
# result = 0
# que = Queue(100000)
# que.enqueue(N)

# while not que.isEmpty():
#     current = que.dequeue()

#     if current == K:
#         result = visit[current]
#         break
#     bfs(current, current+1)
#     bfs(current, current-1)
#     bfs(current, current*2)

# print(result)