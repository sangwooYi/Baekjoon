import sys
sys.stdin = open("baek13913.txt")


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



def hide_and_seek(n, k):
    visited = [-1] * 100001
    que = Queue(100000)
    visited[n] = 0
    que.enqueue((n, 0))

    while not que.is_empty():
        now, time = que.dequeue()
        if now == k:
            idx = now
            while idx != n:
                path.append(idx)
                idx = visited[idx]
            path.append(n)
            return time
        if now+1 < 100001 and visited[now+1] == -1:
            que.enqueue((now+1, time+1))
            visited[now+1] = now
        if now-1 >= 0 and visited[now-1] == -1:
            que.enqueue((now-1, time+1))
            visited[now-1] = now
        if now*2 < 100001 and visited[now*2] == -1:
            que.enqueue((now*2, time+1))
            visited[now*2] = now
        

N, K = map(int, input().split())
path = []
answer = hide_and_seek(N, K)

print(answer)
# 역추적할때 이거 잘 기억하자, 여기서 *의 역할은 unpacking! arr = [1, 2, 3, 4] => *arr = 1 2 3 4 로 출력해주는게 *역할
# [::-1] 의 역할은 해당 배열을 거꾸로 만들어주는 역할!
print(*path[::-1])